#!/usr/bin/python3
"""A module that defines a student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialization function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """converts attributes to json"""
        result = {}
        attrs = [i for i in dir(self) if i[:2] != '__'
                 and not callable(getattr(self, i))]
        for i in attrs:
            try:
                result[i] = getattr(self, i)
            except:
                pass
        return result
