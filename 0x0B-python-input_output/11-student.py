#!/usr/bin/python3
"""Student class module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns specified student attributes
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(json, k, v)
