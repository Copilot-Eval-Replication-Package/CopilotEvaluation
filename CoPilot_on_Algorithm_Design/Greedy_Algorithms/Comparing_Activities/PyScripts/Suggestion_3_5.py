

def check_overlap(activity1, activity2):
    if activity1.end_time < activity2.start_time:
        return True
    elif activity1.end_time == activity2.start_time:
        return True
    else:
        return False
