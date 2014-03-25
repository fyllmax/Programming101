#Imports
import unittest
from solutin import is_number_balanced


#Test

class test_solution(unittest.TestCase):
    """Testing the unit"""
    def test_is_number_balanced(self):

        self.assertTrue(True, is_number_balanced(9))
        # True
        self.assertTrue(True, is_number_balanced(11))
        # True
        self.assertFalse(False, is_number_balanced(13))
        # False
        self.assertTrue(True, is_number_balanced(121))
        # True
        self.assertTrue(True, is_number_balanced(4518))
        # True
        self.assertFalse(False, is_number_balanced(28471))
        # False
        self.assertTrue(True, is_number_balanced(1238033))
        # True

#Program Run
if __name__ == '__main__':
    unittest.main()
