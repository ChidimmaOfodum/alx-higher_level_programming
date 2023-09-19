#!/usr/bin/python3
"""A module containing square class definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """A function that initializes instances of a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter function for size"""
        return self.height

    @size.setter
    def size(self, size):
        """setter function for size"""
        self.width = size
        self.height = size

    def __str__(self):
        """A custom __str__ function, prints with a specific format"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """A function that updates the attributes using args"""
        attr = ['id', 'size', 'x', 'y']
        length = len(args)

        if (args is not None and length != 0):
            for i in range(length):
                setattr(self, attr[i], args[i])
        else:
            for i in list(kwargs.keys()):
                setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """Dictionary representation of a square"""

        result = {
            'id': self.id,
            'size': self.height,
            'x': self.x,
            'y': self.y
        }
        return result
