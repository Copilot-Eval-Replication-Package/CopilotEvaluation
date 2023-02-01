

class Set:
    def __init__(self, activities):
        self.activities = activities

    def add_activity(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            for i in range(len(self.activities)):
                if check_overlap(activity, self.activities[i]):
                    print('Activity overlaps with other activities')
                    break
                elif activity.start_time >= self.activities[i].end_time:
                    self.activities.insert(i, activity)
                    break
                elif activity.end_time <= self.activities[-1].start_time:
                    self.activities.append(activity)
                    break
                else:
                    print('Activity is not added')

