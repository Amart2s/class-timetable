from ortools.sat.python import cp_model
import pandas as pd
from classes import TimeSlot
from classes import Room

rooms = [Room("Lec 1", 60), Room("Lec 2", 60), Room("Tut 1", 25), Room("Tut 2", 20), Room("Tut 3", 20), Room("Tut 4", 15)]

rows = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
columns = ["9:00am", "10:00am", "11:00am", "12:00am", "1:30pm", "2:30pm", "3:30pm", "4:30pm"]

data = [[None for _ in range(len(columns))] for _ in range(len(rows))]

df = pd.DataFrame(data, index=rows, columns=columns)

for column in columns:
    for row in rows:
        if column != "12:00am":
            df.loc[row, column] = TimeSlot(row, column, {room: None for room in rooms})

df["12:00am"] = "Mass/Lunch"

print(df.T)