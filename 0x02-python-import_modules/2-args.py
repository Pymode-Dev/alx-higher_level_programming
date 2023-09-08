#!/usr/bin/python3
import sys

length = len(sys.argv) - 1

if length > 0:
    print("{} {}:".format(length, "arguments" if length > 1 else "argument"))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("0 arguments.")
