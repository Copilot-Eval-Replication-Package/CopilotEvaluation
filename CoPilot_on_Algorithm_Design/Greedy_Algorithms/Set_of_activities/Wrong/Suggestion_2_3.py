

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)
        self.sort_by_end_time()

    def sort_by_end_time(self):
        self.activities.sort(key=lambda x: x.end_time)

    def check_overlap(self, activity):
        if len(self.activities) == 0:
            return True
        else:
            return check_overlap(self.activities[-1], activity)

    def add_activity_if_possible(self, activity):
        if self.check_overlap(activity):
            self.add_activity(activity)

