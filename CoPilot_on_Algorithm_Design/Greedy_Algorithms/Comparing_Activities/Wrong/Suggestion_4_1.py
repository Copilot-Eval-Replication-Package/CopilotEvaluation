

def check_overlap(activity1, activity2):
    activities = [activity1, activity2]
    activities.sort(key=lambda x: x.start_time, reverse=True)
    if activities[1].start_time < activities[0].end_time:
        return False
    elif activities[1].end_time < activities[0].end_time:
        return False
    elif activities[1].start_time == activities[0].start_time:
        return False
    elif activities[1].end_time == activities[0].end_time:
        return False
    elif activities[1].start_time == activities[0].start_time:
        return False
    else:
        return True

