import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_calculate_payment(self):
        name = "RENE"
        worked_hours = ['MO10:00-11:00', 'MO11:00-12:00', 'TU10:00-11:00', 'TU11:00-12:00', 'TH1:00-2:00', 'TH2:00-3:00', 'SA14:00-15:00', 'SA15:00-16:00', 'SA16:00-17:00', 'SA17:00-18:00', 'SU20:00-21:00']
        test_employee = Employee(name, worked_hours)
        test_employee.calculate_payment()
        actual = test_employee.total_payment
        expected = 215

        self.assertEqual(actual,expected)




