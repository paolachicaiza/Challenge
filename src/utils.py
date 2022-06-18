def generate_shift_intervals(schedule):
    start_time = int(schedule[0:2])
    end_time = int(schedule[6:8])
    adjusted_end_time = end_time if end_time > start_time else (end_time + 24)
    intervals = []

    for i in range(start_time, adjusted_end_time):
        interval = f"{i % 24}:00-{(i + 1) % 24}:00"
        intervals.append(interval)
    return intervals


def generate_worked_intervals(tokenized_worked_hours):
    intervals = []
    for tokenized_worked_hour in tokenized_worked_hours:
        day = tokenized_worked_hour[0:2]
        start_time = int(tokenized_worked_hour[2:4])
        end_time = int(tokenized_worked_hour[8:10])

        for i in range(start_time, end_time):
            interval = f"{day}{i}:00-{i + 1}:00"
            intervals.append(interval)

    return intervals
