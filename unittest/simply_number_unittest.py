from os import system
system('cls')
import unittest

from simply_number import simp_num

class TestSimplyNum(unittest.TestCase):
    
    def test_simply_num_true(self):
        self.assertEqual(simp_num(13), True)

    def test_simply_num_false(self):
        self.assertFalse(simp_num(10))

    def test_comparison(self):
        self.assertIsNot(simp_num(10), simp_num(17))
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
