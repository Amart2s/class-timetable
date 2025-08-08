class Subject():
    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher
    
    def __repr__(self):
        return f"{self.subject}, {self.teacher}, hours: {self.duration}"
    
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
    def __init__(self, day, time):
        self.day = day
        self.time = time
    
    def __repr__(self):
        return f"{self.day} at {self.time}"

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
