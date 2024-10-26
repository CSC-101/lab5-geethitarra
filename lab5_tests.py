import data
import lab5
import unittest
from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        time1 = data.Time(4,6,70)
        time2 = data.Time(55,69,20)
        expected = (60, 16, 30)
        result = lab5.time_add(time1,time2)
        self.assertEqual(expected, result)

    def test_time_add2(self):
        time1 = data.Time(2,100,0)
        time2 = data.Time(2,100,20)
        expected = (7, 20, 20)
        result = lab5.time_add(time1,time2)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending(self):
        values = [10, 9, 8, 7]
        expected = True
        result = lab5.is_descending(values)
        self.assertEqual(expected, result)

    def test_is_descending2(self):
        values = [10, 11, 8, 7]
        expected = False
        result = lab5.is_descending(values)
        self.assertEqual(expected, result)
    # Part 5
    def test_largest_between(self):
        values = [10, 11, 8, 7]
        lower = 0
        upper = 4
        expected = 1
        result = lab5.largest_between(values, lower, upper)
        self.assertEqual(expected, result)

    def test_largest_between2(self):
        values = [10, 11, 8, 7, 1000, 7]
        lower = 3
        upper = 6
        expected = 4
        result = lab5.largest_between(values, lower, upper)
        self.assertEqual(expected, result)

    def test_largest_between3(self):
        values = [8, 7, 1000, 7]
        lower = 9
        upper = 2
        expected = None
        result = lab5.largest_between(values, lower, upper)
        self.assertEqual(expected, result)

    def test_largest_between4(self):
        values = [8, 7, 1000, 7, 700000]
        lower = 2
        upper = 100
        expected = 4
        result = lab5.largest_between(values, lower, upper)
        self.assertEqual(expected, result)

    # Part 6
    def test_furthest_from_origin(self):
        values = [Point(3,4), Point(6, 9), Point (100, 600)]
        expected = 2
        result = lab5.furthest_from_origin(values)
        self.assertEqual(expected, result)

    def test_furthest_from_origin2(self):
        values = []
        expected = None
        result = lab5.furthest_from_origin(values)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
