#!/usr/bin/python3
"""
2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """
    is_same_class - returns True if the object is exactly an
    instance of the class
    Args:
        obj: the object
        a_class: the main class
    Return: bool
    """
    return issubclass(a_class, type(obj))
