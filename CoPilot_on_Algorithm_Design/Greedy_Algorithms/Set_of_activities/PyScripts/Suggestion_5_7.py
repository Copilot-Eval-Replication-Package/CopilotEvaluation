

class Set:
    def __init__(self, activities):
        self.activities = sorted(activities, key=lambda activity: activity.end_time)

    def add_activity(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
        else:
            if check_overlap(activity, self.activities[-1]):
                return
            else:
                self.activities.append(activity)
                self.activities = sorted(self.activities, key=lambda activity: activity.end_time)

