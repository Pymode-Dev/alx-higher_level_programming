#!/usr/bin/python3
"""
12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    pascal_triangle: calculate pascal triangle
    Args:
        n: the nth triangle
    Return:
        list of lists
    """
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        pascal.append([1] * (i+1))

    for i in range(2, n):
        for k in range(1, i):
            pascal[i][k] = pascal[i - 1][k - 1] + pascal[i - 1][k]

    return pascal
