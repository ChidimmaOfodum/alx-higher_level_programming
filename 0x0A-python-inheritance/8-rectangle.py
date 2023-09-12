#!/usr/bin/python3

"""A module that defines a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialization function"""

        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height
