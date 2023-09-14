#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = []
    for key, val in a_dictionary.items():
        if val == value:
            values.append(key)

    for k in values:
        del a_dictionary[k]
    return a_dictionary
