

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if activity.start_time >= self.activities[i].end_time:
                    self.activities.insert(i, activity)
                    break
                elif i == len(self.activities) - 1:
                    self.activities.append(activity)
                    break
                else:
                    continue
        return self.activities

    def print_activities(self):
        for activity in self.activities:
            print(f"Activity start time: {activity.start_time}")
            print(f"Activity end time: {activity.end_time}")
            print("\n")
        return self.activities

