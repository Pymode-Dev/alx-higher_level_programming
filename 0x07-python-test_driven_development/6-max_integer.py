#!/usr/bin/python3
"""
Module to  find the max integer in a list
"""


def max_integer(lists=[]):
    """
    max_integer - find the largest integer
    Args:
        list: list
    Return: int|None
    """
    if len(lists) == 0:
        return None
    result = lists[0]
    length = len(lists)
    i = 1
    while i < length:
        if lists[i] > result:
            result = lists[i]
        i += 1
    return result
