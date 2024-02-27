#!/usr/bin/python3
"""
Write the firstclass Base:
"""


class Base:
    """
    class:
        Base - the base class for all class in this project
    Method:
        None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ - initialize a new class
        Args:
            id: None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
