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
        if (list_dictionaries is None and len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)
