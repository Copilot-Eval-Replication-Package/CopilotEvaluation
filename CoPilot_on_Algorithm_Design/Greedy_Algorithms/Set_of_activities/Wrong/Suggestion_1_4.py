

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if not self.activities:
            self.activities.append(activity)
        else:
            for index, act in enumerate(self.activities):
                if compare_activities(act, activity):
                    self.activities.insert(index, activity)
                    break
            else:
                self.activities.append(activity)

    def __str__(self):
        return str(self.activities)



