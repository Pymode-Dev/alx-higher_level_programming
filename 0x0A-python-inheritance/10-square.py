#!/usr/bin/python3
"""nherits from base class."""
Rectangle = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    """
    class
        Retangle - it inherits from base geometry
    Args:
        width, height
    """
    def __init__(self, size):
        """Initialize a new rectangle using BaseGeometry"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calclates the area of a rectangle"""
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
