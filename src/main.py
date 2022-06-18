from employee import Employee
from input_data import InputData


def process_payroll():
    input_data = InputData()
    input_data.read_data("data.txt")
    input_data.parse_lines()

    for employee_name in input_data.employee_worked_hours:
        employee = Employee(employee_name, input_data.employee_worked_hours[employee_name])
        employee.calculate_payment()
        employee.print_payment()


if __name__=="__main__":
    process_payroll()
