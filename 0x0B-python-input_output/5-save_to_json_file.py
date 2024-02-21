#!/usr/bin/python3
"""Writes an object to a text file using JSON rep."""


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an object to a text file using a
    JSON representatin.
    Args:
        my_obj: the object to save
        filename: the filename to save the onbject to
    Return:
        None
    """
    import json

    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
