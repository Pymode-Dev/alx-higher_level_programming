#!/usr/bin/python3
"""
The use of getter and setter in OOP in Python
"""


class Square:
    """
    Class: Square
    Method: Area, getter, and setter
    """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return int(self.__size) ** 2
