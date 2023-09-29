#!/usr/bin/python3
"""
A Magic class matching assembly code
"""

import math


class MagicClass:
    """
    A circle.
    """
    def __init__(self, radiu=0):
        """
        Initialize a magic class
        Args:
            radius: [float | int] - The radius of a circle
        """
        self.__radius = 0
        if isinstance(radius, int) is False and isinstance(radius, float) is False:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of a circle
        """
        return (self.__radius **  2)

    def circumference(self):
        """
        Calculates the circumference of a circle
        """
        return (2 * math.pi * self.__radius)
