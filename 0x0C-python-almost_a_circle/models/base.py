#!/usr/bin/python3
"""
base.py
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return f"{list_dictionaries}"
