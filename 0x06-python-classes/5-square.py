#!/usr/bin/python3
"""
A Square class that calculates area and print out a diagrammatic square.
"""


class Square:
    """
    Class: Square
    method: area, get_size, set_value, print_square image
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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("{}".format(self.__size * '#'))
