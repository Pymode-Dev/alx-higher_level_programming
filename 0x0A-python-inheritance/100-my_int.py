#!/usr/bin/python3
"""A class that inherits from int"""


class MyInt(int):
    """Invert integer operators."""

    def __eq__(self, value):
        """Override the equal to behaviour"""
        return self.real != value

    def __ne__(self, value):
        """Override the not equal to behaviour"""
        return self.real == value
