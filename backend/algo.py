from constraint import Problem
import data

problem = Problem()

problem.addVariables([s for s in data.subjects], data.time_slots)

for student, subjects in data.students.items():
    for i in range(len(subjects)):
        for j in range(i + 1, len(subjects)):
            problem.addConstraint(lambda t1, t2: t1 != t2, (subjects[i], subjects[j]))

solution = problem.getSolution()

if solution:
    print("Valid timetable:")
    for subject, time in sorted(solution.items(), key=lambda x: x[1]):
        print(f"{subject:10} -> {time}, Students: {[s for s in data.students if s in data.subjects[subject]]}")
else:
    print('No valid timetable found.')