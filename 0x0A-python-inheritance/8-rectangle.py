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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
