

class Set:
    def __init__(self):
        self.activities = []

    def __str__(self):
        return str(self.activities)

    def add_activity(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
            return
        elif check_overlap(activity, self.activities[0]):
            return
        elif check_overlap(self.activities[-1], activity):
            return
        else:
            for i in range(len(self.activities)):
                if activity.start_time < self.activities[i].start_time:
                    self.activities.insert(i, activity)
                    return
            self.activities.append(activity)

