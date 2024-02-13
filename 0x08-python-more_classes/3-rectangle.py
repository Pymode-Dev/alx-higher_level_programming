#!/usr/bin/python3
"""A rectangle class with area and perimeter calculated."""


class Rectangle:
    """Rectangle class implementatin."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width mst be an integr")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value,  int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """calculate area."""
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter."""
        if 0 in (self.__width, self.__height):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Print 3 in retangle form."""
        output = ""
        if 0 in (self.__width, self.__height):
            return ""
        for i in range(0, self.__height):
            output += "{}\n".format('#' * self.__width)
        return output
