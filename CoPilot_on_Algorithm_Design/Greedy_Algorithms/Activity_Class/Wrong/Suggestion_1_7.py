

class Activity():
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return "start_time: {}, end_time: {}".format(self.start_time, self.end_time)

    def __repr__(self):
        return "Activity({}, {})".format(self.start_time, self.end_time)