#!/usr/bin/python3
"""
1-write_file.py
"""


def write_file(filename="", text=""):
    """
    write_file: write to file
    Args:
        filename: the file to write to
        text: the text to write
    Return:
        word_count: int
    """
    word_count = 0

    with open(filename, mode="w", encoding="utf-8") as file:
        for word in text:
            file.write(word)
            word_count += 1
    return word_count
