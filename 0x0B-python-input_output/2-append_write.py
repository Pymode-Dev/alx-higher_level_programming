#!/usr/bin/python3
"""Appends text to a text file."""


def append_write(filename="", text=""):
    """
    append_write - a function that appends a string at the end of a
    text file and returns no of char appended.
    Args:
        filename: the filename to append to
        text: the text to append
    Return:
        n: int - the no of char written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        n = f.write(text)
        return n
