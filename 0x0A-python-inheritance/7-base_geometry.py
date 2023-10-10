#!/usr/bin/python3
"""
5-base_geometry.py
"""


class BaseGeometry:
    """
    Class: BaseGeometry
    """
    def area(self):
        """
        Find area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validation
        """
        if False in (isinstance(value, int), not isinstance(value, bool)):
            raise TypeError("{:s} must be an integer".format(name))
        if int(value) <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
