#!/usr/bin/python3
"""
3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - return isinstance and issubclass
    Args:
        obj
        a_class
    Return:
        bool
    """
    return (isinstance(obj, a_class) or issubclass(a_class, type(obj)))
