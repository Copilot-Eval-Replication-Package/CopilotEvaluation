

# class Activity:
#     def __init__(self, start_time, end_time):
#         self.start_time = start_time
#         self.end_time = end_time
# 
# 
# # implement a function for returning the maximal set of activities that can be done by a single person, given a list of activities. this function should be designed greedily.
# 
# 
# def greedy_activity_selector(activities):
#     result = []
#     i = 0
#     while i < len(activities):
#         result.append(activities[i])
#         j = i + 1
#         while j < len(activities):
#             if check_overlap(activities[i], activities[j]):
#                 j += 1
#             else:
#                 break
#         i = j
#     return result
# 
# 
# # implement a class called activity. each instance of this class has two attributes: start_time and end_time. both should be int numbers between 0 and 24.
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
#                 return "Activity overlaps with another activity"
#         self.activities.append(activity)
#         self.activities.sort(key=lambda activity: activity.end_time)
# 
# #

