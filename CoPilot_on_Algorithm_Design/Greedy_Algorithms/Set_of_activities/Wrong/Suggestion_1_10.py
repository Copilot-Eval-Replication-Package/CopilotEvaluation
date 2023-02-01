

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add_activity(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if compare_activities(self.activities[i], activity):
                    self.activities.insert(i, activity)
                    return
            self.activities.append(activity)