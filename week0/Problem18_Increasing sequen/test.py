#Imports
import unittest
from solution import is_increasing


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_is_increasing(self):

        self.assertTrue(True, is_increasing([1, 2, 3, 4, 5]))
        # True
        self.assertTrue(True, is_increasing([1]))
        # True
        self.assertFalse(False, is_increasing([5, 6, -10]))
        # False
        self.assertFalse(False, is_increasing([1, 1, 1, 1]))
        # False

#Program Run
if __name__ == '__main__':
    unittest.main()
