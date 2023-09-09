#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    result = my_list[:]
    if idx < 0:
        pass
    elif idx >= len(my_list):
        pass
    else:
        result[idx] = element
    return result
