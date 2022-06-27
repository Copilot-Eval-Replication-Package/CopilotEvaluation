

# 
# 
# # implement a class named set. each instance of this class has a list of activities.
# # the activities in the list should be sorted by their finish time and an activity can be added to the list if it starts after the first activity finshes
# # and finishes before the last activity starts. an activity can only be added if it does not overlap with any other activity in the list.
# # before adding an activiy, the list should be sorted by finish time.
# class Set:
#     def __init__(self):
#         self.activities = []
# 
#     def add_activity(self, activity):
#         if self.activities == []:
#             self.activities.append(activity)
#         elif activity.start_time >= self.activities[-1].end_time:
#             self.activities.append(activity)
#         elif activity.end_time <= self.activities[0].start_time:
#             self.activities.insert(0, activity)
#         elif check_overlap(activity, self.activities[0]):
#             print("Activity not added")
#         else:
#             for i in range(len(self.activities)):
#                 if check_overlap(activity, self.activities[i]):
#                     print("Activity not added")
#                     break
#                 elif i == len(self.activities) - 1:
#                     self.activities.append(activity)
#                     break
# 
#     def print_activities(self):
#         for activity in self.activities:
#             print(activity.start_time, " ", activity.end_time)
# 
# 
# # implement a class called activity. each instance of this class has two attributes: start_time and end_time. both should be int numbers between 0 and 24.
# # then, implement a function for comparing two activities. the function should return True if the first activity ends before the second activity starts.
# # the fuction should also check that the activities are not overlapping.
# # finally, implement a class named set. each instance of

