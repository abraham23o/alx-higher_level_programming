#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """My base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string representation
        of list_dictionaries
        """
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def to_dictionary(self):
        """
        public method that returns the dictionary representation of a Rectangle
        """
        return self.__dict__

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        obj = []
        if list_objs is not None:
            for i in list_objs:
                obj.append(i.to_dictionary())
        json_str = cls.to_json_string(obj)
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if len(json_string) == 0 or json_string is None:
            return "[]"
        return json.loads(json_string)
