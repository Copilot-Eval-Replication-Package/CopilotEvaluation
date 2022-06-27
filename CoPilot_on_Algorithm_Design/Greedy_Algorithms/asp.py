# implement a class called activity. each instance of this class has two attributes: start_time and end_time. both should be int numbers between 0 and 24.
class Activity:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


# implement a function for comparing two activities. the function should return True if the first activity ends before the second activity starts.
# the fuction should also check that the activities are not overlapping.
def check_overlap(activity1, activity2):
    if activity1.end_time < activity2.start_time:
        return True
    elif activity1.start_time > activity2.end_time:
        return True
    else:
        return False


# implement a class named set. each instance of this class has a list of activities.
# the activities in the list should be sorted by their finish time and an activity can be added to the list if it starts after the first activity finshes
# and finishes before the last activity starts. an activity can only be added if it does not overlap with any other activity in the list.
# before adding an activiy, the list should be sorted by finish time.
class Set:
    def __init__(self, activities):
        self.activities = activities

    def add(self, activity):
        if activity.start_time < self.activities[-1].end_time and activity.end_time > self.activities[0].start_time:
            self.activities.append(activity)
            self.activities.sort(key=lambda activity: activity.end_time)
        else:
            print("Activity cannot be added")

