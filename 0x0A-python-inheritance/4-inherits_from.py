#!/usr/bin/python3
"""Define a class and object checking function."""


def inherits_from(obj, a_class):
    """
    is_same_class - returns true if the object is exactly
    an instance of the specified class.
    Args:
        obj: the class to check
        a_class: the class to check against obj
    Return:
        true or false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
