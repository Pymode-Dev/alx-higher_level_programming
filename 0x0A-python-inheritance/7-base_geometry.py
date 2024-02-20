#!/usr/bin/python3
"""An empty clas BseGeometry."""


class BaseGeometry:
    """
    class
        BaseGeometry: an empty class
    """
    pass

    def area(self):
        """
        area - it calculates the area of any geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
