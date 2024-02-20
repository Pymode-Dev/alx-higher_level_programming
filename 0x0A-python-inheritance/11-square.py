#!/usr/bin/python3
"""nherits from base class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class
        Square - it inherits from Rctangle
    Args:
        size
    """
    def __init__(self, size):
        """Initialize a new rectangle using BaseGeometry"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
