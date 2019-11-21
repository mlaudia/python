from math import gcd

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def reduction(self):
        div = gcd(self.x, self.y)
        if(div != 0):
            self.x = self.x/div
            self.y = self.y/div
        return self

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if(self.y == 1):
            return str(self.x)
        else:
            return "{0}/{1}".format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac({0}, {1})".format(self.x, self.y)

    def __add__(self, other):  # frac1 + frac2
        result = Frac()
        result.x = self.x * other.y + other.x * self.y
        result.y = self.y * other.y
        return result.reduction()

    def __sub__(self, other):  # frac1 - frac2
        result = Frac()
        result.x = self.x * other.y - other.x * self.y
        result.y = self.y * other.y
        return result.reduction()

    def __mul__(self, other):  # frac1 * frac2
        result = Frac()
        result.x = self.x * other.x
        result.y = self.y * other.y
        return result.reduction()

    def __truediv__(self, other):  # frac1 / frac2
        result = Frac()
        result.x = self.x * other.y
        result.y = self.y * other.x
        return result.reduction()

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        a = float(self)
        b = float(other)
        return(a == b)

    def __ne__(self, other):
        a = float(self)
        b = float(other)
        return(a != b)

    def __lt__(self, other):
        a = float(self)
        b = float(other)
        return(a < b)
        

    def __le__(self, other):
        a = float(self)
        b = float(other)
        return(a <= b)

    def __gt__(self, other):
        a = float(self)
        b = float(other)
        return(a > b)

    def __ge__(self, other):
        a = float(self)
        b = float(other)
        return(a >= b)

    def __float__(self):       # float(frac)
        return float(self.x / self.y)