

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)
        self.sort_activities()

    def sort_activities(self):
        self.activities.sort(key=lambda x: x.end_time)

    def add_new_activity(self, activity):
        if self.activities:
            if check_overlap(self.activities[-1], activity):
                self.add_activity(activity)
        else:
            self.add_activity(activity)

