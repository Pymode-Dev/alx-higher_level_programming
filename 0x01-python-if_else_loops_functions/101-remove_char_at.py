#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""
    for index, w in enumerate(str):
        if index != n:
            new_str += w
    return new_str
