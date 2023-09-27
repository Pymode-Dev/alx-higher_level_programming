#!/usr/bin/python3
"""
A module for Square
"""


class Square:
    """
    A class Square that defines a square
    """
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(size)
        except TypeError:
            print("size must be an integer")
