#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """initialize size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Get the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Check errors and setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print square with character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
