#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """public instance method that defines area"""
        return self.__width * self.__height

    def __str__(self):
        """print string representation of square class"""
        return f"[Rectangle] {self.__width}/{self.__height}"
