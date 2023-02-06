

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if check_overlap(activity, self.activities[i]):
                    return
            self.activities.append(activity)
            self.activities.sort(key=lambda x: x.end_time)

