#!/usr/bin/python3
"""An empty rectangle class"""


class Rectangle:
    """class Rectangle"""
    # class attribute to track the count
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of rectangle class"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of class rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns string representation of an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        obj = ""
        for i in range(self.__height):
            obj += str(self.print_symbol) * self.__width + "\n"
        return obj.strip()

    def __repr__(self):
        """string representation of an object using __repr__ method"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """detect instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
