#!/usr/bin/python3
"""
rectangle.py
"""
from .base import Base


class Rectangle(Base):
    """
    class:
        Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if int(value) <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if int(value) <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if int(value) < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if int(value) < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area: calculates the area of a rectangle.
        Args:
            None
        Return:
            int
        """
        return self.__width * self.__height

    def display(self):
        """
        display: prints a rectangle in # format
        Args:
            None
        Return:
            None
        """
        for i in range(self.__height):
            print("{}{}".format(' '*(self.__x),'#' * self.__width,))

    def update(self, *args, **kwargs):
        length = len(args)
        if args:
            if length == 1:
                self.id = args[0]
            if length == 2:
                self.id = args[0]
                self.__width = args[1]
            if length == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if length == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if length == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
