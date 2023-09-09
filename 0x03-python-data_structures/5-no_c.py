#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for string in my_string:
        if string not in ('c', 'C'):
            new_string += string
    return new_string
