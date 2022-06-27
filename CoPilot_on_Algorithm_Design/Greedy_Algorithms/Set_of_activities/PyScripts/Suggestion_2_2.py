

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)
        self.sort_activities()

    def sort_activities(self):
        self.activities.sort(key=lambda activity: activity.end_time)

