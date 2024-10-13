import math
#polymorphism_demo.py

#Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method.")
#Subclass
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
#Subclass
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)