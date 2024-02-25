#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from  models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__X = x
        self.__y = y
