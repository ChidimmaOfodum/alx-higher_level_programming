#!/usr/bin/python3
"""A module that defines a Class Base"""


class Base():
    """A Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
