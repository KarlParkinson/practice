def activitySelect(start, finish):
    activities = []
    finTime = max(finish)
    for i in xrange(len(start)):
        activity = (start[i], finish[i])
        activities.append(activity)
    activities.sort(key=lambda x: x[1])
    time = 0
    selected = []
    while (time < finTime):
        activity = None
        for act in activities:
            if (act[0] >= time):
                activity = act
                break
        selected.append(activity)
        index = activities.index(act)
        activities.pop(index)
        time = activity[1]
    return selected



print activitySelect([1,3,0,5,8,5], [2,4,6,7,9,9])
