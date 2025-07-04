class Shape:
    def __init__(self, area):
        self.area = area

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(area)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

import math.pi
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(area)
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    