from os import system
system('cls')
import unittest
from triangels import Triangles 

class TestRectangle(unittest.TestCase): 
    def setUp(self) -> None:
        self.tr1 = Triangles(3, 4, 5)
        self.tr2 = Triangles(3, 3, 5)
        self.tr3 = Triangles(9, 12, 15)
        self.tr4 = Triangles(5, 3, 4)
        self.tr5 = Triangles(6, 8, 10)
        

    def test_get_square(self):
        self.assertEqual(self.tr1.area(), self.tr4.area())
        self.assertNotEqual(self.tr1.area(), 16.0)

    def test_sub_triangels_area(self):
        self.assertEqual(self.tr5.area() - self.tr1.area(), 18.0)

    def test_triangels_matching(self):
        self.assertGreater(self.tr5.area(), self.tr1.area())

    def test_triangels_sides(self):
        self.assertIsInstance(self.tr2.a_side, int)
    
    # def test_sub_rects(self):
    #     self.assertEqual(self.r4 - self.r1, self.r5)

   
if __name__ == "__main__":
    unittest.main(verbosity=2)



