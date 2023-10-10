#!/usr/bin/python3
"""
5-base_geometry.py
"""


class BaseGeometry:
    """
    Class: BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is False:
            raise TypeError(f"{name} must be an integer")
        if int(value) <= 0:
            raise ValueError(f"{name} must be greater than 0")
