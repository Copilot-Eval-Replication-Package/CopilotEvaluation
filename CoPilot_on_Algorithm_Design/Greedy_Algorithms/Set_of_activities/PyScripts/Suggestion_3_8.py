

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def sort_activities(self):
        self.activities.sort(key=lambda x: x.end_time)

    def add_sorted_activity(self, activity):
        if len(self.activities) == 0:
            self.add_activity(activity)
        else:
            for i in range(len(self.activities)):
                if check_overlap(self.activities[i], activity):
                    return
            self.add_activity(activity)
            self.sort_activities()

