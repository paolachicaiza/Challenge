import os
import unittest

from input_data import InputData


class TestInputData(unittest.TestCase):
    def test_read_data(self):
        input_data = InputData()
        input_data.read_data("test_data.txt")
        actual = input_data.lines
        self.assertTrue(len(actual) > 0)

    def test_parse_lines(self):
        input_data = InputData()
        input_data.read_data("test_data.txt")
        input_data.parse_lines()
        actual = input_data.employee_worked_hours
        expected = {
            'RENE': ['MO10:00-11:00', 'MO11:00-12:00', 'TU10:00-11:00', 'TU11:00-12:00', 'TH1:00-2:00', 'TH2:00-3:00',
                     'SA14:00-15:00', 'SA15:00-16:00', 'SA16:00-17:00', 'SA17:00-18:00', 'SU20:00-21:00'],
            'ASTRID': ['MO10:00-11:00', 'MO11:00-12:00', 'TH12:00-13:00', 'TH13:00-14:00', 'SU20:00-21:00']}
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
