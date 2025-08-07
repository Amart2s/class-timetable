import pandas as pd
from classes import Block
from classes import Subject

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
times = ["9:00", "10:00", "11:00", "1:30", "2:30", "3:30", "4:30"]

blocks = []
for day in days:
    i = []
    for time in times:
        i.append(Block(day, time, None, None))
    blocks.append(i)

df = pd.DataFrame([
{
    "Day": "Monday",
    "9:00am": blocks[0][0],
    "10:00am": blocks[0][1],
    "11:00am": blocks[0][2],
    "12:00am": "Mass/Lunch",
    "1:30pm": blocks[0][3],
    "2:30pm": blocks[0][4],
    "3:30pm": blocks[0][5],
    "4:30pm": blocks[0][6],
},
{
    "Day": "Tuesday",
    "9:00am": blocks[1][0],
    "10:00am": blocks[1][1],
    "11:00am": blocks[1][2],
    "12:00am": "Mass/Lunch",
    "1:30pm": blocks[1][3],
    "2:30pm": blocks[1][4],
    "3:30pm": blocks[1][5],
    "4:30pm": blocks[1][6],
},
{
    "Day": "Wednesday",
    "9:00am": blocks[2][0],
    "10:00am": blocks[2][1],
    "11:00am": blocks[2][2],
    "12:00am": "Mass/Lunch",
    "1:30pm": blocks[2][3],
    "2:30pm": blocks[2][4],
    "3:30pm": blocks[2][5],
    "4:30pm": blocks[2][6],
},
{
    "Day": "Thursday",
    "9:00am": blocks[3][0],
    "10:00am": blocks[3][1],
    "11:00am": blocks[3][2],
    "12:00am": "Mass/Lunch",
    "1:30pm": blocks[3][3],
    "2:30pm": blocks[3][4],
    "3:30pm": blocks[3][5],
    "4:30pm": blocks[3][6],
},
{
    "Day": "Friday",
    "9:00am": blocks[4][0],
    "10:00am": blocks[4][1],
    "11:00am": blocks[4][2],
    "12:00am": "Mass/Lunch",
    "1:30pm": blocks[4][3],
    "2:30pm": blocks[4][4],
    "3:30pm": blocks[4][5],
    "4:30pm": blocks[4][6],
}
])

df.set_index("Day", inplace=True)

profs = [{"Islam": ["PHI101", "PHI102", "PHI201", "PHI202", "PHI301", "PHI302"],
          "Chavura": ["HIS101", "HIS102", "HIS201", "HIS202", "HIS301", "HIS302"]}]
