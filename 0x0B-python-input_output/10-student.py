#!/usr/bin/python3
"""class that efines Student."""


class Student:
    """
    Class:
        Student - the student class
    method:
        to_json: convert the class to JSON
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - convert the class to JSON.
        Args:
            None
        Return:
            dict
        """
        if isinstance(attrs, list) and \
                all(isinstance(ele, str) for ele in attrs):
                    return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
