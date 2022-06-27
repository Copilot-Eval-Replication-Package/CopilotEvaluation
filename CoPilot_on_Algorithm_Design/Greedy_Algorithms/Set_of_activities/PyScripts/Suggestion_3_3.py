

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)
        self.activities.sort(key=lambda x: x.end_time)

    def __str__(self):
        return str(self.activities)

