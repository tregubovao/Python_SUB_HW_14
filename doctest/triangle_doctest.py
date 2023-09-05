from os import system
system('cls')
from math import sqrt
import doctest

def triangel_area(a_side, b_side, c_side) -> float:
    """
    >>> triangel_area(3, 4, 5)
    6.0

    >>> triangel_area(6, 8, 10)
    24.0

    >>> triangel_area(6, 8, 10) == triangel_area(3, 4, 5)
    False

    >>> triangel_area(6, 8, 10) + triangel_area(3, 4, 5)
    30.0

    """    
    p = (a_side + b_side + c_side) / 2
    area = sqrt(p * (p - a_side) * (p - b_side) * (p - c_side))
    return area    
    
if __name__ == "__main__":
          
    doctest.testmod(verbose=True)