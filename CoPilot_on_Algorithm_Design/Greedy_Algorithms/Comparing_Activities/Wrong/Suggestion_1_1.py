

def greedy_activity_selector(activities):
    result = []
    activities.sort(key=lambda activity: activity.end_time)
    for activity in activities:
        if not result or compare_activities(result[-1], activity):
            result.append(activity)
    return result

