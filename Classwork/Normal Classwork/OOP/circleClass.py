# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter. Take radius as input
from math import pi

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def getPerimeter(self) -> float:
        return round(pi * (self.radius ** 2), 2)
    
    def getArea(self) -> float:
        return round(2 * pi * self.radius, 2)
    
newCircle = Circle(5)

print(newCircle.getPerimeter())

print(newCircle.getArea())