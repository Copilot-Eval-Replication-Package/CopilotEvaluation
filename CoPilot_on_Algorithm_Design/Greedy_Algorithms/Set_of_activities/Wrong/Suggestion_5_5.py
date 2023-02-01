

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if activity.start_time >= self.activities[i].end_time:
                    if i == len(self.activities) - 1:
                        self.activities.append(activity)
                    else:
                        continue
                else:
                    if check_overlap(self.activities[i], activity):
                        print("Activity overlaps with another activity")
                    else:
                        self.activities.insert(i, activity)
        self.activities.sort(key=lambda x: x.end_time)

