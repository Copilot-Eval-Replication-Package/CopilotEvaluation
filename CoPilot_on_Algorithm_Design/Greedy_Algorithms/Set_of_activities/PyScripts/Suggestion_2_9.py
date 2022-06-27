

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add(self, activity):
        if activity.start_time >= self.activities[-1].end_time:
            self.activities.append(activity)
        elif activity.end_time <= self.activities[0].start_time:
            self.activities.insert(0, activity)
        else:
            for i in range(len(self.activities)):
                if check_overlap(activity, self.activities[i]):
                    break
            else:
                self.activities.insert(i, activity)

