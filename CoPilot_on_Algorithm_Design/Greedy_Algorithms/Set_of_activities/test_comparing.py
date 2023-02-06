## you can use below samples to test the code for acitivity selection problem
## there are two type of function to check overlap. it depends on the problem statement, you may need to
## use the one that returns True if there is an overlap or the one that returns False if there is an overlap

#Overlapping activities that returns False if there is an overlap
def check_overlap(activity1, activity2):
            if activity1[1] < activity2[0]:
                return True
            elif activity1[0] > activity2[1]:
                return True
            else:
                return False

#Overlapping activities that returns True if there is an overlap
def check_overlap(activity1, activity2):
            if activity1[1] < activity2[0]:
                return False
            elif activity1[0] > activity2[1]:
                return False
            else:
                return True

#Test#1: the function call could be vary between "add_activity", "add" or "add_sorted_activity"
if __name__ == '__main__':
    ss= Set()
    ls_1 = [(2, 4), (1, 3),(5, 6), (6, 8)]
    for item in ls_1:
        ss.add_activity(item)
    print(ss)

#Test#2: the function call could be vary between "add_activity", "add" or "add_sorted_activity"

if __name__ == '__main__':
    ss= Set()
    ls_1 = [(1, 3),(2, 4),(5, 6), (7, 8)]
    for item in ls_1:
        ss.add_activity(item)
    print(ss)

#Test#3: This tests those classes that need an intial object which is not empty.
#The function call could be vary between "add_activity", "add" or "add_sorted_activity"
#Since the return value is an object of class Set, you can add "print_activities" function into the Set class to print tuples
if __name__ == '__main__':
    ls_int = [(2, 4), (5, 6)]
    ss= Set(ls_int)
    ls_1 = [(1, 3)]
    for item in ls_1:
        ss.add(item)
    print(ss.print_activities())

#Test#4: This tests those classes that need an intial object which is not empty.
#The function call could be vary between "add_activity", "add" or "add_sorted_activity"
if __name__ == '__main__':
    int_ls= [(2, 4),(5, 6)]
    ss= Set(int_ls)
    ls_1 = [ (1, 3), (4,6),(6, 8)]
    for item in ls_1:
        ss.add_activity(item)
    print(ss.print_activities())


#Function to print the activities
def print_activities(self):
        print(self.activities)
