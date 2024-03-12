#!/usr/bin/python3
"""Test class of Rectangle."""
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        ...

    def test_rec(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(1, r1.id)
        r2 = Rectangle(2, 10)
        self.assertEqual(2, r2.id)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12, r3.id)
        r4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(r4.id, 34)
        r5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r5.id, -5)
        r6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r6.id, 9)

    def test_exception(self):
        with self.assertRaises(TypeError) as error:
            r = Rectangle(10, "2")

        exp = error.exception
        s = "height must be an integer"
        self.assertEqual(s, str(exp))
