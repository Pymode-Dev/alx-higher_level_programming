#!/usr/bin/python3
def roman_to_int(roman_string):
    sample = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000
            }
    integer = 0
    prev_int = 0

    if roman_string is None or not roman_string.isalpha():
        return None

    for string in reversed(roman_string):
        current_int = sample[string]

        if current_int > prev_int:
            integer += current_int
        elif current_int == prev_int:
            integer += current_int
        else:
            integer -= current_int
        prev_int = current_int

    return integer
