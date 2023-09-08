#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    length = len(sys.argv)
    total = 0

    for num in range(1, length):
        total += int(sys.argv[num])
    print("{}".format(total))
