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
        return self.size
    
    @size.setter
    def size(self, size):
        self.size = size

    def __str__(self):
        """A custom __str__ function, prints with a specific format"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
