#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for num in list(my_list[::-1]):
        print("{:d}".format(num))
