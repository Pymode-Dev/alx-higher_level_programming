#!/usr/bin/python3
"""
base.py
"""


class Base:
    """
    Class: Base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
