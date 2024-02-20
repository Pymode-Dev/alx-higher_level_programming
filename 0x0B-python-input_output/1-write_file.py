#!/usr/bin/python3
"""Write a file."""



def write_file(filename="", text=""):
    """
    write_file - a function that writes to a text file and returns
    the numer of chaacters written.
    Args:
        filename: The filename to save the text to.
        text: the text to save
    Return:
        n: int
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        n = f.write(text)
        return n
