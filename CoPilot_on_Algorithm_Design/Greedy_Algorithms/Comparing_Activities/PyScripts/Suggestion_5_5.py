

def check_overlap(activity1, activity2):
    if activity1.end_time <= activity2.start_time:
        return False
    else:
        return True

