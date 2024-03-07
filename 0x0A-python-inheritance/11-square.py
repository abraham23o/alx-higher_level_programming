#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Instantiation"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """print string representation of square class"""
        return f"[Square] {self.__size}/{self.__size}"
