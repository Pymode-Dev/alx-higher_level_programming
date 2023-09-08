#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    variable = dir(hidden_4)
    for var in variable:
        if var.startswith("_") is False:
            print("{}".format(var))
