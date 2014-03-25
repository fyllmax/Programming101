#Imports
import unittest
from solution import nth_fibonacci


#Test

class test_solution(unittest.TestCase):
    """Testing the unit"""

    def test_nth_fibonacci(self):
        self.assertEqual(1, nth_fibonacci(2))
        self.assertEqual(2, nth_fibonacci(3))
        self.assertEqual(55, nth_fibonacci(10))


#Program Run
if __name__ == '__main__':
    unittest.main()
