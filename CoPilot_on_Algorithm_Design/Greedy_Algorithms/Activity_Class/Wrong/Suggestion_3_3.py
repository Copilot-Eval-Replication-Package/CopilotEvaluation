

class Activity:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f'Activity({self.start_time}, {self.end_time})'

    def __str__(self):
        return f'({self.start_time}, {self.end_time})'

