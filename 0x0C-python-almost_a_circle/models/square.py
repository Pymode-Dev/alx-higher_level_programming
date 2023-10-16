#!/usr/bin/python3
"""
square.py
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    class: Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        self.width = value

    def update(self, *args, **kwargs):
        if args:
            length = len(args)
            if length == 1:
                self.id = args[0]
            if length == 2:
                self.id = args[0]
                self.width = args[1]
            if length == 3:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
            if length == 4:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('size', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
