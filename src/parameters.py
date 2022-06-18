from src.utils import generate_shift_intervals

workday = ["MO", "TU", "WE", "TH", "FR"]
weekend = ["SA", "SU"]

first_shift = "00:01-09:00"
second_shift = "09:01-18:00"
third_shift = "18:01-00:00"

first_shift_hours = generate_shift_intervals(first_shift)
second_shift_hours = generate_shift_intervals(second_shift)
third_shift_hours = generate_shift_intervals(third_shift)


def get_day_type(day):
    if day in workday:
        return "workday"
    if day in weekend:
        return "weekend"


def get_shift(time_slot):
    if time_slot in first_shift_hours:
        return "first_shift_hours"
    if time_slot in second_shift_hours:
        return "second_shift_hours"
    if time_slot in third_shift_hours:
        return "third_shift_hours"


rates = {
    "workday": {"first_shift_hours": 25, "second_shift_hours": 15, "third_shift_hours": 20},
    "weekend": {"first_shift_hours": 30, "second_shift_hours": 20, "third_shift_hours": 25}
}
