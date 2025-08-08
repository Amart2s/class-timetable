from ortools.sat.python import cp_model
import data
from timetable import df
from classes import Block

model = cp_model.CpModel()

subject_vars = {subject: model.NewIntVar(0, data.NUM_SLOTS - 1, subject) for subject in data.subjects}

for subject in data.subjects:
    for slot in range(data.NUM_SLOTS - 1):  # Avoid slot + 1 overflow
        is_subject_at_slot = model.NewBoolVar(f"{subject}_at_{slot}")
        model.Add(subject_vars[subject] == slot).OnlyEnforceIf(is_subject_at_slot)
        model.Add(subject_vars[subject] != slot).OnlyEnforceIf(is_subject_at_slot.Not())

        for other_subject in data.subjects:
            if other_subject == subject:
                continue
            # If subject is at slot, then other_subject ≠ slot and ≠ slot + 1
            model.Add(subject_vars[other_subject] != slot).OnlyEnforceIf(is_subject_at_slot)
            model.Add(subject_vars[other_subject] != slot + 1).OnlyEnforceIf(is_subject_at_slot)

for student, subjects in data.students.items():
    for i in range(len(subjects)):
        for j in range(i + 1, len(subjects)):
            s1, s2 = subject_vars[subjects[i]], subject_vars[subjects[j]]
            model.Add(s1 != s2)

for prof, subs in data.professors.items():
    for i in range(len(subs)):
        for j in range(i + 1, len(subs)):
            s1, s2 = subject_vars[subs[i]], subject_vars[subs[j]]
            model.Add(s1 != s2)

max_slot = model.NewIntVar(0, data.NUM_SLOTS - 1, "max_slot")
model.AddMaxEquality(max_slot, list(subject_vars.values()))
model.Minimize(max_slot)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Schedule found:")
    for subject in data.subjects:
        day = solver.Value(subject_vars[subject]) // 5
        time = solver.Value(subject_vars[subject]) % 5
        df.loc[data.days[day], data.time_slots[time]].update_filled_by(subject)
        df.loc[data.days[day], data.time_slots[time + 1]].update_filled_by(subject)
    print(f"Total slots used: {solver.Value(max_slot) + 1}\n")
else:
    print("❌ No valid schedule found.")

print(df.T)   