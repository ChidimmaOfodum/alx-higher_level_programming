#!/usr/bin/python3

"""A module that defines a class"""


class BaseGeometry:
    """A basegeometry class"""

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
