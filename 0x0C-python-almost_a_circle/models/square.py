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

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
