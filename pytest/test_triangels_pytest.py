from os import system
system('cls')
import pytest
from triangels import Triangles

@pytest.fixture
def tr1():
    return Triangles(3, 4, 5)

@pytest.fixture
def tr2():
    return Triangles(6, 8, 10)

@pytest.fixture
def tr3():
    return Triangles(5, 4, 3)


def test_triangels_area(tr1, tr2):
    assert tr1.area() != tr2.area()

def test_triangels_area_2(tr1, tr3):
    assert tr1.area() == tr3.area()

def test_triangels_area_addition(tr1, tr2):
    assert tr1.area() + tr2.area() == 30.0

def test_triangels_area_division(tr1, tr2):
    assert tr2.area() - tr1.area() == 18.0


if __name__ == "__main__":
    pytest.main(['-v'])