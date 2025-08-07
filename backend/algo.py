from ortools.sat.python import cp_model
import data

model = cp_model.CpModel()

subject_vars = {subject: model.NewIntVar(0, data.NUM_SLOTS - 1, subject) for subject in data.subjects_set}

for student, subjects in data.students.items():
    for i in range(len(subjects)):
        for j in range(i + 1, len(subjects)):
            s1, s2 = subject_vars[subjects[i]], subject_vars[subjects[j]]
            model.Add(s1 != s2)

max_slot = model.NewIntVar(0, data.NUM_SLOTS - 1, "max_slot")
model.AddMaxEquality(max_slot, list(subject_vars.values()))
model.Minimize(max_slot)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Schedule found:")
    for subject in data.subjects_set:
        print(f"{subject:10} → {data.time_slots[solver.Value(subject_vars[subject])]}")
    print(f"\n Total slots used: {solver.Value(max_slot) + 1}")
else:
    print("❌ No valid schedule found.")