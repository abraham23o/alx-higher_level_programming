#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize size"""
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Retrieve value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
