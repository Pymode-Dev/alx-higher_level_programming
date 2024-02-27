#!/usr/bin/python3
"""Test base clas"""
import unittest

from models.base import Base


class testBase(unittest.TestCase):
    def setUp(self):
        Base.base__nb_objects = 0

    def test_inst(self):
        b1 = Base()
        self.assertEqual(1, b1.id)
        a = Base(12)
        self.assertEqual(12, a.id)
        b = Base()
        b2 = Base()
        self.assertEqual(3, b2.id)
        b4 = Base()
        self.assertEqual(4, b4.id)
