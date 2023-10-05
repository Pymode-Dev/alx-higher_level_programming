#!/usr/bin/python3
"""
5-text_indentation - module
"""


def text_indentation(text):
    """
    text_indentation - indent text according to some punctuation symbols
    Args:
        text: str
    Return:
        None
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    count = 0

    while count < len(text) and text[count] == " ":
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == '\n' or text[count] in ".?:":
            if text[count] in ".?:":
                print('\n')
            count += 1
            while count < len(text) and text[count] == " ":
                count += 1
                continue
        count += 1
