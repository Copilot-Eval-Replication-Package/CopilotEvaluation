

def check_overlap(activity1, activity2):
    if activity2.start_time < activity1.end_time:
        return False
    elif activity2.end_time < activity1.end_time:
        return False
    elif activity2.start_time == activity1.start_time:
        return False
    elif activity2.end_time == activity1.end_time:
        return False
    elif activity2.start_time == activity1.start_time:
        return False
    else:
        return True

