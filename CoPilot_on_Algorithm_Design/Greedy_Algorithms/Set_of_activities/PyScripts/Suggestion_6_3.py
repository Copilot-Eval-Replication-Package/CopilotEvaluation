

class Set:
    def __init__(self):
        self.activity_list = []

    def add_activity(self, activity):
        self.activity_list.append(activity)
        self.activity_list.sort(key=lambda activity: activity.end_time)

    def add_activities(self, activity_list):
        for activity in activity_list:
            self.add_activity(activity)

    def get_activity_list(self):
        return self.activity_list

