#!/usr/bin/python3
def element_at(my_list, idx):
    result = None
    if idx < 0:
        result = None
    elif idx >= len(my_list):
        result = None
    else:
        result = my_list[idx]
    return result
