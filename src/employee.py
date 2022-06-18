from src.parameters import get_day_type, get_shift, rates


class Employee:
    def __init__(self,name, worked_hours):
        self.name = name
        self.worked_hours = worked_hours
        self.total_payment = 0

    def calculate_payment(self):
        payment = []
        for hour in self.worked_hours:
            day = hour[0:2]
            day_type = get_day_type(day)
            time_slot = hour[2:]
            shift = get_shift(time_slot)
            pay = rates[day_type][shift]
            payment.append(pay)
        self.total_payment = sum(payment)

    def print_payment(self):
        print(f"The amount to pay {self.name} is: {self.total_payment} USD")
