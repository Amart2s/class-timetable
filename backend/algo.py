from ortools.sat.python import cp_model
import pandas as pd
from classes import TimeSlot
from classes import Room
from data import subjects, students, teachers, NUM_SLOTS, days, times

rooms = [Room("Lec 1", 60), Room("Lec 2", 60), Room("Tut 1", 25), Room("Tut 2", 20), Room("Tut 3", 20), Room("Tut 4", 15)]

data = [[None for _ in range(len(times))] for _ in range(len(days))]

df = pd.DataFrame(data, index=days, columns=times)

for time in times:
    for day in days:
        if time != "12:00am":
            df.loc[day, time] = TimeSlot(day, time, {room: None for room in rooms})

df["12:00am"] = "Mass/Lunch"

model = cp_model.CpModel()

subject_vars = {subject: model.NewIntVar(0, NUM_SLOTS - 1, subject) for subject in subjects}



print(df.T)