#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        expected_result = None
        actual_result = max_integer([])
        self.assertEqual(expected_result, actual_result)

    def test_real_integer(self):
        int_list = [1, 3, 5, 7, 10, 9]
        expected_result = 10
        actual_result = max_integer(int_list)
        self.assertEqual(expected_result, actual_result)

    def test_int_and_float(self):
        actual_result = max_integer([1, 1.5, 2, 3.2, 5, 5.4])
        expected_result = 5.4
        self.assertEqual(expected_result, actual_result)

    def test_float(self):
        actual_result = max_integer([2.5, 5.5, 3.5, 4.5])
        expected_result = 5.5
        self.assertEqual(expected_result, actual_result)

    def test_negative_int(self):
        actual_result = max_integer([-10, -5, -8, -3])
        expected_result = -3
        self.assertEqual(expected_result, actual_result)

    def test_positive_and_negative(self):
        actual_result = max_integer([-7, 15, -2, 10, 0])
        expected_result = 15
        self.assertEqual(expected_result, actual_result)

    def test_repeated_int(self):
        actual_result = max_integer([5, 5, 4, 4, 3, 3, 6, 6])
        expected_result =  6
        self.assertEqual(expected_result, actual_result)

    def test_big_int(self):
        actual_result = max_integer([10000, 999999, 1000000])
        expected_result = 1000000
        self.assertEqual(expected_result, actual_result)

    def test_one_int(self):
        actual_result = max_integer([42])
        expected_result = 42
        self.assertEqual(expected_result, actual_result)
