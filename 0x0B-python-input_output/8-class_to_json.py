#!/usr/bin/python3
"""Returns the dictionary description with simple data structure."""


def class_to_json(obj):
    """
    class_to_json - a function that returns the dict description
    with simple ds.
    Args:
        obj: the object to transform  dict
    Return:
        dict
    """
    return obj.__dict__
