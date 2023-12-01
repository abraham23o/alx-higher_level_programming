#!/usr/bin/python3

def uppercase(str):
    new_str = '';
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            upper_ch = chr(ord(ch) - ord('a') + ord('A'))
            new_str += upper_ch
        else:
            new_str += ch

    print(new_str)
