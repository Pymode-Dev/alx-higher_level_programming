#!/usr/bin/python3
"""
0-read_file.py
"""
import sys


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            sys.stdout.write(line)
