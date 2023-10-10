#!/usr/bin/python3
"""
4-from_json_string.py
"""
import json


def from_json_string(my_str):
    """
    from_json_string: load from JSON format to python object
    Args:
        my_str: the JSON format
    Return:
        python object
    """
    output = json.loads(my_str)
    return output
