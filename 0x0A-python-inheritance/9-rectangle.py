#!/usr/bin/python3
"""nherits from base class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class
        Retangle - it inherits from base geometry
    Args:
        width, height
    """
    def __init__(self, width, height):
        """Initialize a new rectangle using BaseGeometry"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calclates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
