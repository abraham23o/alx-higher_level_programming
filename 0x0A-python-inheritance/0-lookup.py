#!/usr/bin/python3
"""
returns list of attributes
and methods in a class
"""


def lookup(obj):
    """
    return list of all methods
    and attributes in a class
    """
    return dir(obj)
