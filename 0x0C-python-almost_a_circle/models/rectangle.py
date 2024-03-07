#!/usr/bin/python3
"""My class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """My class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        if not isinstance(width, int) or isinstance(width, bool):
            raise TypeError("width must be an integer")
        if not isinstance(height, int) or isinstance(height, bool):
            raise TypeError("height must be an integer")
        if not isinstance(x, int) or isinstance(x, bool):
            raise TypeError("x must be an integer")
        if not isinstance(y, int) or isinstance(y, bool):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @property
    def height(self):
        """get the height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, val):
        """set the width"""
        if not isinstance(val, int) or isinstance(val, bool):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """set the height"""
        if not isinstance(val, int) or isinstance(val, bool):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @x.setter
    def x(self, val):
        """set x"""
        if not isinstance(val, int) or isinstance(val, bool):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @y.setter
    def y(self, val):
        """set y"""
        if not isinstance(val, int) or isinstance(val, bool):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """gets the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print a rectangle using '#"""
        rect = ""
        rect += "\n" * self.__y
        for i in range(self.__height):
            rect += '' * self.__x
            rect += '#' * self.__width
            if i < self.__height - 1:
                rect += '\n'
        print(rect)

    def __str__(self):
        """string representation of an object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        for i in range(min(len(args), 5)):
            arg = args[i]
            if i == 0:
                self.id = arg
            elif i == 1:
                self.__width = arg
            elif i == 2:
                self.__height = arg
            elif i == 3:
                self.__x = arg
            else:
                self.__y = arg
