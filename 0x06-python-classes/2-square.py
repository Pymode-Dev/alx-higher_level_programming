#!/usr/bin/python3
"""
A module for Square
"""


class Square:
    """
    A class Square that defines a square
    """
    def __init__(self, size=0):
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif (type(size) is not int):
            raise TypeError("size must be an integer")
        self.__size = size
