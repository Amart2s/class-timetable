students = {
    "Alice": ["Math", "Science", "English"],
    "Bob": ["History", "Literature", "Science"],
    "Jerry": ["PE", "Math", "Literature", "History"],
    "Kate": ["Philosophy", "PE", "Math", "English"]
}

subjects = {
    "Math": [student for student in students if "Math" in students[student]],
    "Science": [student for student in students if "Science" in students[student]],
    "English": [student for student in students if "English" in students[student]],
    "History": [student for student in students if "History" in students[student]],
    "Literature": [student for student in students if "Literature" in students[student]],
    "PE": [student for student in students if "PE" in students[student]],
    "Philosophy": [student for student in students if "Philosophy" in students[student]]
}

time_slots = ["9:00am", "10:30am", "12:00am", "1:30pm"]

print(subjects)