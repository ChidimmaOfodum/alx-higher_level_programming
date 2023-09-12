#!/usr/bin/python3

"""A module that defines a class"""


class BaseGeometry:
    """A basegeometry class"""

    def area(self):
        """an area function not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the input 'value'
        Args:
            name: name of the input 
            value: value associated to the name
        Raises: 
            TypeError: if value not an integer
            ValueError: if value <= 0
        """

        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
