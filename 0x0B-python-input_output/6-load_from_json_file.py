#!/usr/bin/python3
"""Creates an object from a JSON file"""


def load_from_json_file(filename):
    """
    load_from_json_file - a function that creates an object
    from a JSON file.
    Args:
        filename: the filename to creates the object from
    Return:
        None
    """
    import json

    with open(filename) as f:
        json.load(f)
