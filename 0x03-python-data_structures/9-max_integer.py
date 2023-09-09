#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        result = None
    else:
        result = sorted(my_list, reverse=True)
    return result[0]
