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

    @property
    def size(self):
        """
        get the value of size or width
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        updates height and width
        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        public method that assigns attributes
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """public method that returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
