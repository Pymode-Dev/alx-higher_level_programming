#!/usr/bin/python3
"""
A class Square that defines a square and has a method that
claculates the area of a Square.
"""


class Square:
    """
    Square class with method that calculates the area of a Square.
    """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
