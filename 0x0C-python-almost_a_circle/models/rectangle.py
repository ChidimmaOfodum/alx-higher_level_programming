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
        return self.width
    
    @width.setter
    def width(self, width):
        self.width = width

    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, height):
        self.height = height
    
    @property
    def x(self):
        return self.x
    
    @x.setter
    def x(self, x):
        self.x = x
    
    @property
    def y(self):
        return self.y
    
    @y.setter
    def y(self, y):
        self.y = y

