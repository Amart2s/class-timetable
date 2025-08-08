import sys

class Subject():
    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher
    
    def __repr__(self):
        return f"{self.subject}, {self.teacher}"
    
    def lecture(self, timeslots):
        self.lec = Lecture(self.subject, timeslots)

    def tutorial(self, timeslots):
        self.tut = Tutorial(self.subject, timeslots)

class Lecture():
    def __init__(self, subject, timeslots):
        self.subject = subject
        self.timeslots = timeslots

class Tutorial():
    def __init__(self, subject, timeslots):
        self.subject = subject
        self.timeslots = timeslots


class TimeSlot():
    def __init__(self, day, time, filled_by):
        self.day = day
        self.time = time
        self.filled_by = filled_by
    
    def __repr__(self):
        for item in self.filled_by.values():
            lst = ""
            if item:
                if not lst:
                    lst += f"{item}"
                else:
                    lst += f"/{item}"
        if lst:
            return lst
        return "None"
    
    def fill_slot(self, room, subject):
        if not self.filled_by[room]:
            self.filled_by[room] = subject
        else:
            sys.exit("Room already filled!")


class Teacher():
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"{self.name}"
    
class Room():
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return f"The {self.name} room, fits {self.size}"
