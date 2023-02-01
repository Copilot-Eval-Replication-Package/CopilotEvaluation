

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add_activity(self, activity):
        self.activities.append(activity)
        self.activities = sorted(self.activities, key=lambda activity: activity.end_time)

    def is_valid(self, activity):
        for i in self.activities:
            if check_overlap(i, activity):
                return False
        return True

    def __str__(self):
        return str(self.activities)