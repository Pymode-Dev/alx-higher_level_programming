#!/usr/bin/python3
"""Return a JSON representation of an object."""


def to_json_string(obj):
    """
    to_json_string - a function that returns a JSON rep of an object.
    Args:
        obj: the object to return its JSON rep
    Return:
        JSON
    """
    import json

    return json.dumps(obj)
