#!/usr/bin/python3
"""
1-my_list.py
"""


class MyList(list):
    """
    class:
        MyList - a class that inherits from list
    method:
        print_sorted - prints the list but sorted
    """
    def print_sorted(self):
        print(sorted(self))
