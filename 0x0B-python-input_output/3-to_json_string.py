#!/usr/bin/python3
"""
3-to_json_string.py
"""
import json


def to_json_string(obj):
    """
    to_json_string: write to json format
    Args:
        obj: the object format to transform
    Return:
        JSON io
    """
    output = json.dumps(obj)
    return output
