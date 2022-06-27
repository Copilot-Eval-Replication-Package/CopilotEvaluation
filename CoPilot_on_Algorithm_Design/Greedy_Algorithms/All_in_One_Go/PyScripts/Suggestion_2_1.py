

# 
# 
# def check_overlap(activity1, activity2):
#     if activity1.end_time < activity2.start_time:
#         return True
#     elif activity1.start_time > activity2.end_time:
#         return True
#     else:
#         return False
# 
# 
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
# def main():
#     activity1 = Activity(4, 6)
#     activity2 = Activity(2, 9)
#     activity3 = Activity(3, 5)
#     activity4 = Activity(1, 7)
#     activity5 = Activity(6, 8)
#     activity6 = Activity(7, 9)
#     set1 = Set()
#     set1.add_activity(activity1)
#     set1.add_activity(activity2)
#     set1.add_activity(activity3)
#     set1.add_activity(activity4)
#     set1.add_activity(activity5)
#     set1.add_activity(activity6)
#

