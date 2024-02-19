#!/usr/bin/python3
"""
lookup - a function that returns the list of available attr and methods of an object
"""


def lookup(obj):
    """
    lookup - return the available attributes and methods of an object
    Args:
        - obj: the object to look up
    Return:
        list of available of attributes and methods
    """
    return dir(obj)
