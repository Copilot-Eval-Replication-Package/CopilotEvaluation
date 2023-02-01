

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add_activity(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
        elif check_overlap(self.activities[-1], activity):
            return
        else:
            self.activities.append(activity)
        self.activities.sort(key=lambda x: x.end_time)

