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
        """get the x"""
        return self.__x

    @property
    def y(self):
        """get the y"""
        return self.__y
