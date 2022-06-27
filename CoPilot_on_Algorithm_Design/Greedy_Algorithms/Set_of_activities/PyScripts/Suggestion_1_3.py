

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        if not self.activities:
            self.activities.append(activity)
        else:
            if activity.start_time >= self.activities[-1].end_time:
                self.activities.append(activity)
            else:
                for i in range(len(self.activities)):
                    if activity.start_time >= self.activities[i].end_time:
                        self.activities.insert(i, activity)
                        break
                    elif activity.end_time <= self.activities[i].start_time:
                        self.activities.insert(i, activity)
                        break

    def __str__(self):
        return str(self.activities)

