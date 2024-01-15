#!/usr/bin/python3
"""My class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """My class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
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
        self.__width = val

    @height.setter
    def height(self, val):
        """set the height"""
        self.__height = val

    @x.setter
    def x(self, val):
        """set x"""
        self.__x = val

    @y.setter
    def y(self, val):
        """set y"""
        self.__y = val
