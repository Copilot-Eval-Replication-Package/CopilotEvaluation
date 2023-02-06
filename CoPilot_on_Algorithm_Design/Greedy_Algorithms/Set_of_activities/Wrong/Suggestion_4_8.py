

class Set:
    def __init__(self):
        self.activities = []

    def add(self, activity):
        if self.activities == []:
            self.activities.append(activity)
        else:
            last_activity = self.activities[-1]
            if last_activity.end_time < activity.start_time:
                self.activities.append(activity)
            else:
                if check_overlap(last_activity, activity):
                    raise OverlapError
                else:
                    raise NonOverlapError

    def __repr__(self):
        return str(self.activities)

