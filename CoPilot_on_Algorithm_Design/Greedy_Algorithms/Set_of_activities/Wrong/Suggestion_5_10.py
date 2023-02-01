

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add(self, activity):
        if activity.start_time < self.activities[-1].end_time and activity.end_time > self.activities[0].start_time:
            self.activities.append(activity)
            self.activities.sort(key=lambda activity: activity.end_time)
        else:
            print('Activity cannot be added')