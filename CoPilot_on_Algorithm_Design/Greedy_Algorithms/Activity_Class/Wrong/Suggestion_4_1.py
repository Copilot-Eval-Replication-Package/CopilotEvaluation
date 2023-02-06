

# class Activity:
#     def __init__(self, start_time, end_time):
#         self.start_time = start_time
#         self.end_time = end_time
# 
# 
# # implement a function for comparing two activities. the function should return True if the first activity ends before the second activity starts.
# # the fuction should also check that the activities are not overlapping.
# 
# 
# def check_overlap(activity1, activity2):
#     activities = [activity1, activity2]
#     activities.sort(key=lambda x: x.start_time, reverse=True)
#     if activities[1].start_time < activities[0].end_time:
#         return False
#     elif activities[1].end_time < activities[0].end_time:
#         return False
#     elif activities[1].start_time == activities[0].start_time:
#         return False
#     elif activities[1].end_time == activities[0].end_time:
#         return False
#     elif activities[1].start_time == activities[0].start_time:
#         return False
#     else:
#         return True
# 
# 
# # implement a class named set. each instance of this class has a list of activities.
# # the activities in the list should be sorted by their finish time and an activity can be added to the list if it starts after the first activity finshes
# # and finishes before the last activity starts. an activity can only be added if it does not overlap with any other activity in the list.
# # before adding an activiy, the list should be sorted by finish time.
# 
# 
# class Set:
#     def __init__(self):
#         self.activities = []
# 
#     def add_activity(self, activity):
#         self.activities.sort(key=lambda activity: activity.end_time)
#         for activity_in_set in self.activities:
#             if not check_overlap(activity, activity_in_set):
#                 return "

