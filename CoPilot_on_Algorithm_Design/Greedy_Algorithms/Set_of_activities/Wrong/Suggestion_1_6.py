

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        for i in range(len(self.activities)):
            if compare_activities(activity, self.activities[i]):
                self.activities.insert(i, activity)
                return
        self.activities.append(activity)

    def __str__(self):
        return str(self.activities)

