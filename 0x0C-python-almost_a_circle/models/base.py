#!/usr/bin/python3
"""Module containing the ``Base`` class definition."""
import json


class Base:
    """``Base`` class definition."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes objects of class ``Base``. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json representation of input"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A function that saves json to a file"""
        f_name = cls.__name__

        if (list_objs is None):
            result = "[]"
        else:
            result = [x.to_dictionary() for x in list_objs]
            result = cls.to_json_string(result)

        with open(f"{f_name}.json", 'w') as f:
            f.write(result)

    def from_json_string(json_string):
        """A function that returns object from json string"""
        return json.loads(json_string)
