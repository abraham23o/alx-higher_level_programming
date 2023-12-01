#!/usr/bin/python3

def uppercase(str):
    for ch in str + '\n':
        if ord(ch) not in range(97, 123):
            print("{}".format(ch), end="")
        else:
            print("{}".format(chr(ord(ch) - 32)), end="")
