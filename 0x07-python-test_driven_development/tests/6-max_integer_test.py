#!/usr/bin/python3
"""
Unittest for max_integer function
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        expected_result = None
        actual_result = max_integer([])
        self.assertEqual(actual_result, expected_result)

    def test_positive(self):
        expected_result = 4
        actual_result = max_integer([1, 3, 2, 4])
        self.assertEqual(actual_result, expected_result)

    def test_negative_list(self):
        expected_result = -1
        actual_result = max_integer([-4, -3, -2, -1])
        self.assertEqual(actual_result, expected_result)

    def test_string_in_list(self):
        expected_result = "ball"
        actual_result = max_integer(["a", "askell", "ball"])
        self.assertEqual(actual_result, expected_result)

    def test_float_in_list(self):
        expected_result = 3.4
        actual_result = max_integer([1, 2, 3.4, 3, 3.34])
        self.assertEqual(actual_result, expected_result)

    def test_all_float(self):
        expected_result = 5.5
        actual_result = max_integer([1.5, 5.5, 5.49, 2.5, 3.9])
        self.assertEqual(actual_result, expected_result)

    def test_empty_string(self):
        expected_result = None
        actual_result = max_integer("")
        self.assertEqual(actual_result, expected_result)

    def test_one_element(self):
        expected_result = 9
        actual_result = max_integer([9])
        self.assertEqual(actual_result, expected_result)
