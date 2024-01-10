#!/usr/bin/python3
"""
function that adds a string to a txt file
"""


def append_write(filename="", text=""):
    """adds a string to a txt file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
