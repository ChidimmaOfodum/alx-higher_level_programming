#!/usr/bin/python3

"""A module that defines a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialization function
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            """
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """a method that returns area of shape
        Args:
            size: size of shape
        Returns:
            area of shape
        """

        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

r = Rectangle(3, 5)

print(r)
print(r.area())
