#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """
    read_file - a function that reads a text fileand prints to
    stdout.
    Args:
        filename: the text filename to read
    Return:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        r = f.read()
        print(r)
