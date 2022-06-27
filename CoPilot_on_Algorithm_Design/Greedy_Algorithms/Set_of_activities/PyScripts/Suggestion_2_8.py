

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add(self, activity):
        for i in range(len(self.activities)):
            if check_overlap(self.activities[i], activity):
                break
        else:
            self.activities.append(activity)
        self.activities.sort(key=lambda x: x.end_time)

