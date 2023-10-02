#!/usr/bin/python3
"""
A rectangle implementation that has widht and height and can calculates
area and perimeter
"""


class Rectangle:
    """
    class:
        Rectangle
    atrribute:
        width - width of a rectangle
        height - height of a rectangle
    method:
        area - calculate the area of a rectangle
        perimeter- calculates the perimeter of a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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

    def area(self) -> int:
        """
        calculates area of a rectangle
        """
        return int(self.width) * int(self.height)

    def perimeter(self) -> int:
        """
        calculates the perimeter of a rectangle
        """
        if 0 in (self.width, self.height):
            return 0
        return (int(self.width) + int(self.height)) * 2
