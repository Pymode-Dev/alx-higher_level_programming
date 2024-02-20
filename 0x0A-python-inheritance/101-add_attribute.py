#!/usr/bin/python3
"""Add new attribute to class"""


def add_attribute(obj, att, value):
    """
    add_attribute - add new attribute if possible

    Args:
        obj: the man class
        att: attribute name to add
        value: attribute value to add
    Raise:
        TypeError: can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
