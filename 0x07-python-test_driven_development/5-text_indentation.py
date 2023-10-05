#!/usr/bin/python3
def text_indentation(text):
    for i in text:
        if i in ".?:":
            print(i, end="")
            print("\n")
        else:
            print(i, end="")
