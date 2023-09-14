#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    div = sum([l[1] for l in my_list])
    weight = sum([l[0] * l[1] for l in my_list])
    return weight / div
