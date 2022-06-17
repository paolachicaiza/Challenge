def generate_time_intervals(schedule):
    start_time = int(schedule[0:2])
    end_time = int(schedule[6:8])
    adjusted_end_time = end_time if end_time>start_time else (end_time+24)
    intervals=[]

    for i in range(start_time,adjusted_end_time):
        interval = f"{i%24}:00-{(i+1)%24}:00"
        intervals.append(interval)
    return intervals