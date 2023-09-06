#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if j == 9 and i == 8:
            print("{}{}".format(i, j))
            break
        print("{}{}".format(i, j), end=", ")
