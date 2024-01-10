#!/usr/bin/python3
"""
function that writes a string to a txt file
"""


def write_file(filename="", text=""):
    """write a string to a txt file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
