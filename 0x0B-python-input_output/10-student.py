#!/usr/bin/python3
"""
10-student.py
"""


class Student:
    """
    class:
        Student
    attributes:
        first_name, last_name, age
    method:
        to_json: return JSON format
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            if all(isinstance(elem, str) for elem in attrs):
                return {
                        key: getattr(self, key)
                        for key in attrs
                        if hasattr(self, key)
                        }
        class_dict = self.__dict__
        return class_dict
