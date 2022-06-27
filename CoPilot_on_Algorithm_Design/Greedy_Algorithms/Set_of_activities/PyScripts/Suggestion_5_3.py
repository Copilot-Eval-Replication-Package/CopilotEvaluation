

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)
        self.activities.sort(key=lambda x: x.end_time)

    def add_activities(self, activities):
        for activity in activities:
            self.add_activity(activity)

    def __str__(self):
        return str([str(activity) for activity in self.activities])

