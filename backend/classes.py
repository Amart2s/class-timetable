"""
when creating a subject, want:
- class ID
- How many lectures/tutorials/semenars, how long is each
- size of class for each lec/sem/tut
- prof of class
"""

class Subject():

    def __init__(self, subject, ):
        self.subject = subject
    
    def get_size(self):
        return self.size
    
    def get_length(self):
        return self.length
    
    def get_subject(self):
        return self.subject

class Block:
    def __init__(self, day, start, room=None, filled_by=None):
        self.day = day
        self.start = start
        self.filled_by = filled_by
        self.room = room
    
    def __repr__(self):
        return f"{self.filled_by}"

class Timetable:
    def __init__(self):
        self.blocks = []