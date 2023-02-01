

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
            return
        for i in range(len(self.activities)):
            if check_overlap(activity, self.activities[i]):
                return
        for i in range(len(self.activities)):
            if activity.start_time >= self.activities[i].end_time:
                self.activities.insert(i, activity)
                return
        self.activities.append(activity)

