

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add_activity(self, activity):
        if self.activities == []:
            self.activities.append(activity)
            return
        elif compare_activities(activity, self.activities[-1]):
            self.activities.append(activity)
            return
        else:
            for i in range(len(self.activities)):
                if compare_activities(activity, self.activities[i]):
                    self.activities.insert(i, activity)
                    return
            self.activities.append(activity)
            return

