#!/usr/bin/python3
"""Mdule to find the max integer in a list"""


def max_integer(lst=[]):
    """Find the maximum integer in a list."""
    if len(lst) == 0:
        return None
    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result
