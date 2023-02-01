

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if activity.start_time >= self.activities[i].end_time:
                    self.activities.insert(i, activity)
                    break
            else:
                self.activities.append(activity)

    def __str__(self):
        return str(self.activities)

