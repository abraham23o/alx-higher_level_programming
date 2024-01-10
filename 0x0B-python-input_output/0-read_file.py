#!/usr/bin/python3
"""
Function that reads a file and outputs
it to the stdout
"""


def read_file(filename=""):
    """reads and prints out content of a file"""
    with open(filename, encoding="utf-8") as f:
        data_read = f.read()
        print(data_read, end="")
