

class Set:
    def __init__(self, activities):
        self.activities = activities
        self.activities.sort(key=lambda activity: activity.end_time)

    def add_activity(self, activity):
        if check_overlap(self.activities[0], activity):
            return False
        elif check_overlap(activity, self.activities[-1]):
            return False
        else:
            self.activities.append(activity)
            self.activities.sort(key=lambda activity: activity.end_time)
            return True

