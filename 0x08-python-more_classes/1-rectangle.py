#!/usr/bin/python3
"""A module that defines a Rectangle class"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(self.__width) != int):
            raise TypeError("width must be an integer")
        elif (self.__width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(self.__height) != int):
            raise TypeError("height must be an integer")
        elif (self.__height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
