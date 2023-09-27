#!/usr/bin/python3
"""
A module with Square class and a private attribute of size
"""


class Square:
    """
    A class Square that defines a square
    """
    def __init__(self, size):
        """
        Initialize the class
        Args:
            size: int - the size of a square
        """
        self.__size = size
