#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    rom_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_lst = list(roman_string.upper())
    res = 0
    prev = 0

    for i in rom_lst:
        if i in rom_vals:
            res += rom_vals[i]
            if rom_vals[i] > prev:
                res -= prev * 2
            prev = rom_vals[i]
        else:
            return 0
    return res

    # for i in roman_string:
    #     if i == 'M':
    #         res += 1000
    #     elif i == 'D':
    #         res += 500
    #     elif i == 'C':
    #         res += 100
    #     elif i == 'L':
    #         res += 50
    #     elif i == 'X':
    #         res += 10
    #     elif i == 'V':
    #         res += 5
    #     elif i == 'I':
    #         res += 1
    # return res