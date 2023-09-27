#!/usr/bin/python3
"""
A Square class is defined.
"""


class Square:
    """
    class: Square
    method: area, getter, setter, my_print, position
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif False in (isinstance(value[0], int), isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return int(self.__size) ** 2

    def my_print(self):
        if int(self.__size) == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(int(self.__size)):
                print("{}".format(' ' * self.__position[0]), end="")
                print("{}".format(self.__size * '#'))
