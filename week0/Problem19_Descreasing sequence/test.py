#Imports
import unittest
from solution import is_decreasing


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_is_decreasing(self):

        self.assertTrue(True, is_decreasing([5, 4, 3, 2, 1]))
        # True
        self.assertFalse(False, is_decreasing([1, 2, 3]))
        # False
        self.assertTrue(True, is_decreasing([100, 50, 20]))
        # True
        self.assertFalse(False, is_decreasing([1, 1, 1, 1]))
        # False


#Program Run
if __name__ == '__main__':
    unittest.main()
