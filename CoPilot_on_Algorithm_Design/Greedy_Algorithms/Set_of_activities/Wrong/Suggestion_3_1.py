

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
        elif activity.start_time >= self.activities[-1].end_time:
            self.activities.append(activity)
        elif check_overlap(self.activities[-1], activity):
            return False
        else:
            self.activities.append(activity)
        self.activities.sort(key=lambda activity: activity.end_time)
        return True

