#!/usr/bin/python3
"""A module that defines a student class"""


class Student:
    """A Student class"""

    def __init__(self, first_name, last_name, age):
        """initialization function
        Args:
            first_name(int): first name of student
            last_name(int): last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """converts attributes to json
        Args:
            attrs: attributes to be converted to JSON
        Returns:
            attribute in json format
        """
        result = {}
        if attrs is None:
            attrs = [i for i in dir(self) if i[:2] != '__'
                     and not callable(getattr(self, i))]
        for i in attrs:
            try:
                result[i] = getattr(self, i)
            except Exception:
                pass
        return result

    def reload_from_json(self, json):
        """Changes the attributes of an object to the json values"""
        self.last_name = json.get("first_name", self.first_name)
        self.first_name = json.get("last_name", self.last_name)
        self.age = json.get("age", self.age)
