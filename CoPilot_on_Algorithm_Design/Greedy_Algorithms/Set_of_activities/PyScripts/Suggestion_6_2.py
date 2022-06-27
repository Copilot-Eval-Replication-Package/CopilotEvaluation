

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        elif activity.start_time >= self.activities[-1].end_time:
            self.activities.append(activity)
        elif activity.end_time <= self.activities[0].start_time:
            self.activities.insert(0, activity)
        elif check_overlap(activity, self.activities[0]):
            print("Activity not added")
        else:
            for i in range(len(self.activities)):
                if check_overlap(activity, self.activities[i]):
                    print("Activity not added")
                    break
                elif i == len(self.activities) - 1:
                    self.activities.append(activity)
                    break

    def print_activities(self):
        for activity in self.activities:
            print(activity.start_time, " ", activity.end_time)

