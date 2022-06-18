import unittest

from utils import generate_shift_intervals, generate_worked_intervals


class MyTestCase(unittest.TestCase):
    def test_generate_shift_intervals(self):
        schedule = '10:00-12:00'
        actual = generate_shift_intervals(schedule)
        expected = ['10:00-11:00', '11:00-12:00']
        self.assertEqual(actual, expected)  # add assertion here

    def test_generate_worked_intervals(self):
        schedule = ['MO10:00-12:00']
        actual = generate_worked_intervals(schedule)
        expected = ['MO10:00-11:00', 'MO11:00-12:00']
        self.assertEqual(actual, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
