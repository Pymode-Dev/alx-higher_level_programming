#!/usr/bin/python3
"""
rectangle implementation in class
"""


class Rectangle:
    """
    class: Rectangle
    attributes: width, height
    methods: area, perimeter, __str__, __repr__, __del__
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """calculates area"""
        return int(self.width) * int(self.height)

    def perimeter(self):
        """calculates perimeter"""
        if 0 in (self.width, self.height):
            return (0)
        return (int(self.width) + int(self.height)) * 2

    def __str__(self):
        if 0 in (self.width, self.height):
            return ""

        string = ['#' * self.__width for i in range(self.__height)]
        return "\n".join(string)

    def __repr__(self):
        rect = "Rectangle("+str(self.__width)+", "+str(self.__height)
        rect += ")"
        return rect

    def __del__(self):
        type(self).number_of_instances -= 1
        print("bye rectangle...")
