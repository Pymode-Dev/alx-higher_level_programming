#!/usr/bin/python3
append_write = __import__("2-append_write").append_write

nb_char = append_write("file_append.txt", "This School is so cool!\n")
print(nb_char)
