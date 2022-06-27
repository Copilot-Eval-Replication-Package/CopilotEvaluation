

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            if check_overlap(activity, self.activities[-1]):
                print("overlap")
            else:
                self.activities.append(activity)
            self.activities.sort(key=lambda x: x.end_time)

