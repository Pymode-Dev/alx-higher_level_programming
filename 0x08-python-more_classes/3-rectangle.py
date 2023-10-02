#!/usr/bin/python3
"""
A rectangle class with area, perimeter method with __str__ implementation
"""


class Rectangle:
    """
    class:  Rectangle
    attribute: width, height
    method: __str__, area, perimeter
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates area of a rectangle
        """
        return int(self.width) * int(self.height)

    def perimeter(self):
        """
        calculates the perimeter of a rectangle
        """
        if 0 in (self.width, self.height):
            return 0
        return (int(self.width) + int(self.height)) * 2

    def __str__(self):
        """
        print ascii rectangle
        """
        string = ""
        if 0 in (self.width, self.height):
            string = " "
        else:
            for i in range(self.height):
                string += "{}\n".format('#' * self.width)
        return string
