#!/usr/bin/python3
"""
8-class_to_json.py
"""


def class_to_json(obj):
    """
    class_to_json: convert all class attributes to JSON
    Args:
        obj: the class to convert
    Return:
        python dict
    """
    return obj.__dict__
