#!/usr/bin/python3
"""module tha contains rectangle"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instance of class ``Rectangle``."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """``width`` property."""
        return self.__width

    @width.setter
    def width(self, value):
        """width property getter"""
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """``height`` property. """
        return self.__height

    @height.setter
    def height(self, value):
        """height property getter"""
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """``x`` property  getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """x property getter"""
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """``y`` property getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """y property getter"""
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Returns the area of the Rectangle. """
        return self.width * self.height

    def display(self):
        """prints in hashed format using width and height"""
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """custom __str__ function with a specific format"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
        )

    def update(self, *args, **kwargs):
        """updates a particular key attribute"""
        if (args is not None and len(args) != 0):
            length = len(args)
            attr = ['id', 'width', 'height', 'x', 'y']

            for i in range(length):
                setattr(self, attr[i], args[i])
        else:
            for i in list(kwargs.keys()):
                setattr(self, i, kwargs[i])
