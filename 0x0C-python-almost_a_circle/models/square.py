# /usr/bin/python3
"""A module that defines a square class"""

from rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A custom __str__ function"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
