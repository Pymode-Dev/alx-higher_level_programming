#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    result = []
    if idx < 0:
        pass
    elif idx > len(my_list):
        pass
    else:
        my_list[idx] = element
    return my_list
