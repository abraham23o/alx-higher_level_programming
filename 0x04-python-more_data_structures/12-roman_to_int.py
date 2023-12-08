#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    for i in roman_string:
        if i == 'M':
            res += 1000
        elif i == 'D':
            res += 500
        elif i == 'C':
            res += 100
        elif i == 'L':
            res += 50
        elif i == 'X':
            res += 10
        elif i == 'V':
            res += 5
        elif i == 'I':
            res += 1
    return res