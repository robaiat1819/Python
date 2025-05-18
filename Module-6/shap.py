from math import pi


class Shape:
    def __init__(self, name):
        self.name = name


class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width


class Circel(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return self.pi * self.radius * self.radius
