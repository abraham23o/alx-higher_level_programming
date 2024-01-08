#!/usr/bin/python3
"""
   function that adds 2 numbers
"""


def add_integer(a, b=98):
    """Adds 2 integers
    Args:
        a (int | float): first int to add
        b (int |float): second int to add, default = 98

    Returns:
        an integer, the addition of a and b

    Raises:
        TypeError: if 'a' or 'b' is not an int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
