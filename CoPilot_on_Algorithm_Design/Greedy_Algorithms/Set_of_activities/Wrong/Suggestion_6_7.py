

class Set:
    def __init__(self, activity_list):
        self.activity_list = activity_list

    def add_activity(self, activity):
        self.activity_list.append(activity)
        self.activity_list.sort(key=lambda x: x.end_time)

    def __str__(self):
        return str(self.activity_list)

