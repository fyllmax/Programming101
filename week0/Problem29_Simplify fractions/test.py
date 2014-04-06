#Imports
import unittest
from solution import simplify_fraction


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_simplify_fraction(self):

        self.assertEqual((1, 3), simplify_fraction((3, 9)))
        # (1,3)
        self.assertEqual((1, 7), simplify_fraction((1, 7)))
        # (1,7)
        self.assertEqual((2, 5), simplify_fraction((4, 10)))
        # (2,5)
        self.assertEqual((3, 22), simplify_fraction((63, 462)))
        # (3,22)

#Program Run
if __name__ == '__main__':
    unittest.main()
