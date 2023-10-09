#!/usr/bin/python3
"""
0-lookup.py
"""


def lookup(obj):
    """
    lookup - function that returns the list of available attributes
    and methods of an object
    Args:
        obj: the object
    Return: list
    """
    return dir(obj)
