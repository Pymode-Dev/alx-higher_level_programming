#!/usr/bin/python3
"""
print_square - module
"""


def print_square(size):
    """
    print_square - print square according to the size
    Args:
        size: int
    Return:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if int(size) < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and int(size) < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
