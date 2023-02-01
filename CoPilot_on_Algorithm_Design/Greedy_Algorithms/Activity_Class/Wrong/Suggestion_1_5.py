

class activity:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
    def __lt__(self, other):
        return self.end_time < other.end_time

