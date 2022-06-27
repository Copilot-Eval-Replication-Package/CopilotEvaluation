

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        self.activities.append(activity)
        self.activities.sort(key=lambda activity: activity.end_time)

