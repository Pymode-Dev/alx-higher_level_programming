#!/usr/bin/python3
"""
101-add_attribute.py
"""


def add_attribute(obj, key, value):
    if hasattr(obj, '__dict__'):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new wttribute")
