#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    def __init__(self, number):
        self.__number = number

    def __eq__(self, n):
        return self.__number != n

    def __ne__(self, n):
        return self.__number == n
