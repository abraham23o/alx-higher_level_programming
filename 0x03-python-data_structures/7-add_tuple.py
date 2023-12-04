#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    j1 = tuple_a[0] if tuple_a else 0
    j2 = tuple_b[0] if tuple_b else 0
    k1 = tuple_a[1] if (tuple_a and len(tuple_a) > 1) else 0
    k2 = tuple_b[1] if (tuple_b and len(tuple_b) > 1) else 0
    return j1 + j2, k1 + k2
