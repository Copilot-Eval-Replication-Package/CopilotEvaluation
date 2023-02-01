

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add_activity(self, activity):
        if len(self.activities) == 0:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if check_overlap(activity, self.activities[i]):
                    print("Activity overlaps with another activity in the set")
                    return False
            self.activities.append(activity)
            self.activities.sort(key=lambda x: x.end_time)
        return True

    def get_activities(self):
        return self.activities

