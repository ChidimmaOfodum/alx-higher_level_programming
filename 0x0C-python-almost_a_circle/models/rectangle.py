#!/usr/bin/python3
"""A module that defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization function"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if (type(width) is not int):
            raise TypeError('width must be an integer')
        elif (width <= 0):
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if (type(height) is not int):
            raise TypeError('height must be an integer')
        elif (height <= 0):
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if (type(x) is not int):
            raise TypeError('x must be an integer')
        elif (x < 0):
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if (type(y) is not int):
            raise TypeError('y must be an integer')
        elif (y < 0):
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """area of a rectangle"""
        return (self.width * self.height)

    def display(self):
        """display function"""
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        return ("[Rectangle]({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        ))

    def update(self, *args, **kwargs):
        if (args is not None and len(args) != 0):
            length = len(args)
            attr = ['id', 'width', 'height', 'x', 'y']

            for i in range(length):
                setattr(self, attr[i], args[i])
        else:
            for i in list(kwargs.keys()):
                setattr(self, i, kwargs[i])
