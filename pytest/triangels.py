from os import system
system('cls')
from math import sqrt

class UnrealTriangleError(Exception):
    
    def __init__(self, a_side, b_side, c_side) -> None:
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def __str__(self) -> str:
        return f'Треугольника со сторонами {self.a_side}, {self.b_side} и {self.c_side} НЕ существует'

class Triangles:

    def __init__(self, a_side, b_side, c_side) -> None:
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def area(self) -> str:
        if (self.a_side + self.b_side > self.c_side 
            and self.a_side + self.c_side > self.b_side 
            and self.c_side + self.b_side > self.a_side):
            p = (self.a_side + self.b_side + self.c_side) / 2
            _area = sqrt(p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side))
            return _area
        raise UnrealTriangleError(self.a_side, self.b_side, self.c_side)
    
    def __sub__(self, other: 'Triangles'):
        a = self.a_side - other.a_side
        b = self.b_side - other.b_side
        c = self.c_side - other.c_side
        return Triangles(a, b, c)
    
    def __str__(self) -> str:
        return f'Треугольник со сторонами {self.a_side}, {self.b_side} и {self.c_side}'

# tr1 = Triangles(3, 4, 5)
# tr2 = Triangles(3, 3, 5)
# tr3 = Triangles(9, 12, 15)

# print(tr3 - tr1)