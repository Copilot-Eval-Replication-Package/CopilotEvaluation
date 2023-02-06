

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add(self, activity):
        self.activities.append(activity)
        self.activities.sort(key=lambda x: x.end_time)

    def __repr__(self):
        return str(self.activities)

