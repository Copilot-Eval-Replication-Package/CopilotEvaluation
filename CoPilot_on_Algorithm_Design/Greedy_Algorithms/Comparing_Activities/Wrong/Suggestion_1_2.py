

def greedy_activity_selection(activities):
    # sort the activities in non-decreasing order of their end times
    activities.sort(key=lambda x: x.end_time)
    # create an empty list to store the selected activities
    selected_activities = []
    # select the first activity
    selected_activities.append(activities[0])
    # iterate over the remaining activities
    for activity in activities[1:]:
        # if the current activity overlaps with the last selected activity
        if activity.start_time >= selected_activities[-1].end_time:
            # add the current activity to the selected activities
            selected_activities.append(activity)
    return selected_activities

