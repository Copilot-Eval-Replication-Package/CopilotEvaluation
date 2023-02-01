

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add_activity(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
            return
        for i in range(len(self.activities)):
            if activity.start_time >= self.activities[i].end_time:
                self.activities.insert(i, activity)
                return
        else:
            self.activities.append(activity)

    def get_activities(self):
        return self.activities

