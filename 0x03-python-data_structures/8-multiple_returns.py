#!/usr/bin/python3
def multiple_returns(sentence):
    result = ""

    if sentence == "":
        result = (0, None)
    else:
        new = tuple(sentence)
        first = new[0]
        result = (len(new), first)
    return result
