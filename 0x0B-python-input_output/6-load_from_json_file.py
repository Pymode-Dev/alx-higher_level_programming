#!/usr/bin/python3
"""
6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file: load JSON format from file to python object
    Args:
        filename: the file to load from
    Return:
        Python Object
    """
    with open(filename, mode="r") as file:
        output = json.load(file)
        return output
