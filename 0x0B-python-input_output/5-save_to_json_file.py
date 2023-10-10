#!/usr/bin/python3
"""
5-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file: save python object format to JSON format file
    Args:
        my_obj: python object
        filename: the file tp save it to
    Return:
        None
    """
    with open(filename, mode="w")  as file:
        json.dump(my_obj, file)
