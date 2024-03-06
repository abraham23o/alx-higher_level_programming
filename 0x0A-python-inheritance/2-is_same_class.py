#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    returns true if obj is exactly
    an instance of a_class, else false
    """
    return type(obj) is a_class
