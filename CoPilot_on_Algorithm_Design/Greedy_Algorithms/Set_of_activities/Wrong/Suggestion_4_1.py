

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
        else:
            if activity.start_time >= self.activities[-1].end_time:
                self.activities.append(activity)
            else:
                for i in range(len(self.activities)):
                    if check_overlap(self.activities[i], activity):
                        break
                else:
                    self.activities.append(activity)
        self.activities.sort(key=lambda x: x.end_time)

    def __str__(self):
        return str(self.activities)

