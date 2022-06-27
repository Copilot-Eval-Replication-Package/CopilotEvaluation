

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if self.activities:
            if activity.start_time >= self.activities[-1].end_time:
                self.activities.append(activity)
        else:
            self.activities.append(activity)

    def __str__(self):
        return str(self.activities)

