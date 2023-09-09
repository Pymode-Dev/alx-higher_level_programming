#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        result = None
    else:
        result = sorted(my_list, reverse=True)[0]
    return result
