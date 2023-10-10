#!/usr/bin/python3
"""
4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    inherits_from - if true object
    Args:
        obj, a_class
    Return: bool
    """
    return (issubclass(type(obj), a_class) and
            not type(obj) is a_class)
