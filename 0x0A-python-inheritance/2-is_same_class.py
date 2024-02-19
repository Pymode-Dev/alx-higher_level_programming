#!/usr/bin/python3
"""
2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """
    is_same_class - returns true if the object is exactly
    an instance of the specified class.
    Args:
        obj: the class to check
        a_class: the class to check against obj
    Return:
        true or false
    """
    return type(obj) == a_class
