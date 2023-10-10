#!/usr/bin/python3
"""
0-read_file.py
"""


def read_file(filename=""):
    """
    read_file: read file to stdout
    Args:
        filename: the filepath
    Return:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
