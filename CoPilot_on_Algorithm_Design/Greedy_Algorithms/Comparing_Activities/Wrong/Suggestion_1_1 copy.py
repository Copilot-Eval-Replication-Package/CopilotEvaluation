def check_overlap(activity1, activity2):
    if activity1[1] < activity2[0]:
        return False
    elif activity1[0] > activity2[1]:
        return False
    elif activity1[0] == activity2[0]:
        return False
    elif activity1[1] == activity2[1]:
        return False
    else:
        return True



if __name__ == '__main__':
    
    ls_1 = [(2, 4), (1, 3)]
    print(check_overlap((1, 3),(4, 5)))