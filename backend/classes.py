class Subject:
    def __init__(self, subject, length, size):
        self.subject = subject
        self.length = length
        self.size = size
    
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