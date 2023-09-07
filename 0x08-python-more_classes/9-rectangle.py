#!/usr/bin/python3
"""A module that defines a rectangle class"""


class Rectangle:
    """A rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (isinstance(rect_1, Rectangle) != True):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (isinstance(rect_2, Rectangle) != True):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_1.area() == rect_2.area()
                    or rect_1.area() > rect_2.area()):
                return rect_1
            return rect_2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        result = 0
        if (self.width != 0 and self.height != 0):
            result = 2 * (self.__width + self.__height)
        return result

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        result = ""
        if (self.width == 0 or self.height == 0):
            return result
        for i in range(self.height):
            result += str(self.print_symbol) * self.width
            if (i != self.height - 1):
                result += "\n"
        return result

    def __repr__(self):
        result = f"Rectangle({self.width}, {self.height})"
        return result

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
