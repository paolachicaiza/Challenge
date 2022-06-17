from utils import generate_time_intervals

workday = ["MO", "TU", "WE", "TH", "FR"]
weekend = ["SA", "SU"]

first_shift = "00:01-09:00"
second_shift = "09:01-18:00"
third_shift = "18:01-00:00"

first_shift_hours = generate_time_intervals(first_shift)
second_shift_hours = generate_time_intervals(second_shift)
third_shift_hours = generate_time_intervals(third_shift)