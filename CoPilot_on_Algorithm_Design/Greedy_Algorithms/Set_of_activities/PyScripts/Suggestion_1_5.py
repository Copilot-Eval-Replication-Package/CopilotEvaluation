

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if len(self.activities) == 0 or activity.start_time >= self.activities[-1].end_time:
            self.activities.append(activity)
        elif activity.end_time <= self.activities[0].start_time:
            self.activities.insert(0, activity)
        else:
            for i in range(len(self.activities)):
                if activity.start_time >= self.activities[i].end_time:
                    self.activities.insert(i, activity)
                    break

    def __str__(self):
        return str(self.activities)

