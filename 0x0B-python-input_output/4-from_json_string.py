#!/usr/bin/python3
"""Load a JSON string to obj."""


def from_json_string(my_str):
    """
    from_json_string - a function that returns object represented
    by a JSON string.
    Args:
        my_str: the string to load from JSON
    Return:
        obj
    """
    import json

    return json.loads(my_str)
