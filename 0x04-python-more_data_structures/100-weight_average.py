#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    div = sum([element[1] for element in my_list])
    weight = sum([element[0] * element[1] for element in my_list])
    return weight / div
