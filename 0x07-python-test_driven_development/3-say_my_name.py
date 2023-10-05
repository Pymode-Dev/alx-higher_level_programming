#!/usr/bin/python3
"""
say_my_name - module
"""

def say_my_name(first_name, last_name=""):
    """
    Print the full name of a user
    Args:
        first_name: str
        last_name: str
    Return:
        None
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
