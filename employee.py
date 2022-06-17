from constants import first_shift_hours, workday, weekend, second_shift_hours, third_shift_hours


class Employee:
    def __init__(self,name, worked_hours):
        self.name = name
        self.worked_hours = worked_hours
        self.total_payment = 0

    def calculate_payment(self):
        payment = []
        for hour in self.worked_hours:
            day = hour[0:2]
            time_slot = hour[2:]
            if time_slot in first_shift_hours:
                if day in workday:
                    pay = 25
                if day in weekend:
                    pay = 30
            if time_slot in second_shift_hours:
                if day in workday:
                    pay = 15
                if day in weekend:
                    pay = 20
            if time_slot in third_shift_hours:
                if day in workday:
                    pay = 20
                if day in weekend:
                    pay = 25
            payment.append(pay)
        self.total_payment = sum(payment)

    def print_payment(self):
        print(f"The amount to pay {self.name} is: {self.total_payment} USD")
