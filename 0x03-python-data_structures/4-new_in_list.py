#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None: 
        return
    lst = my_list.copy()
    if idx > len(lst) - 1 or idx < 0:
        return lst
    lst[idx] = element
    return lst
