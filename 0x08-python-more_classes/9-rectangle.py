#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """
    class: Rectangle
    attribute: width, height
    methods: area, perimeter
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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
        """calculates area"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        if 0 in (self.__width, self.__height):
            return 0
        return (int(self.__width) + int(self.__height)) * 2

    def __str__(self):
        if 0 in (self.__width, self.__height):
            return ""

        string = [str(self.print_symbol) * self.__width for i in range(self.__height)]
        return "\n".join(string)

    def __repr__(self):
        return f"Rectangle({self.__width, self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
