from point import Point
from math import pi, sqrt

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle({}, {}, {})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return pi * self.radius**2

    def move(self, x, y):     # przesuniecie o (x, y)
        self.pt.x += x
        self.pt.y += y
        return self

    def cover(self, other):   # okrąg pokrywający oba
        x_diff = max(self.pt.x, other.pt.x) - min(self.pt.x, other.pt.x)
        y_diff = max(self.pt.y, other.pt.y) - min(self.pt.y, other.pt.y)
        
        x = max(self.pt.x, other.pt.x) - x_diff/2
        y = max(self.pt.y, other.pt.y) - y_diff/2

        #odl od srodka nowego okregu do srodka poprzednich + promien wiekszego
        r = sqrt(x_diff**2 + y_diff**2)/2 + max(self.radius, other.radius)

        return Circle(x, y, r)