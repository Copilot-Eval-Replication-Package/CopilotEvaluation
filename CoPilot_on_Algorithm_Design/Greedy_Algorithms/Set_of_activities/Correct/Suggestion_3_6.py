

class Set:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if check_overlap(self.activities[i], activity):
                    return
                elif i == len(self.activities)-1:
                    self.activities.append(activity)
                    self.activities.sort(key=lambda x: x.end_time)
                    return
                elif activity.start_time < self.activities[i].start_time and activity.end_time < self.activities[i].end_time:
                    self.activities.insert(i, activity)
                    return
                elif activity.start_time > self.activities[i].start_time and activity.end_time > self.activities[i].end_time:
                    continue
                else:
                    self.activities.insert(i, activity)
                    return

    def get_activities(self):
        return self.activities

