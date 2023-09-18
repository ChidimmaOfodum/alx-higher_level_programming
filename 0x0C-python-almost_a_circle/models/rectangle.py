#!/usr/bin/python3
Base = __import__('base').Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if (type(width) is not int):
            raise TypeError('width must be an integer')
        elif (width <= 0):
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if (type(height) is not int):
            raise TypeError('height must be an integer')
        elif (height <= 0):
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) is not int):
            raise TypeError('x must be an integer')
        elif (x < 0):
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) is not int):
            raise TypeError('y must be an integer')
        elif (y < 0):
            raise ValueError('y must be >= 0')
        self.__y = y
    
    def area(self):
        return (self.width * self.height)
    
    def display(self):
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end='')
            print('#' * self.width)
    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
    def update(self, *args):
        length = len(args)
        attr = ['id', 'width', 'height', 'x', 'y']
        
        for i in range(length):
            setattr(self, attr[i], args[i])


