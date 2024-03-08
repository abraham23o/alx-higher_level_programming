#!/usr/bin/python3
"""My class Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """My class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """my Square class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of an object"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
