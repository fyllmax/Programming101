#Imports
import unittest
from solution import contains_digit


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_contains_digit(self):

        self.assertFalse(False, contains_digit(123, 4))
        # False
        self.assertTrue(True, contains_digit(42, 2))
        # True
        self.assertTrue(True, contains_digit(1000, 0))
        # True
        self.assertFalse(False, contains_digit(12346789, 5))
        # False


#Program Run
if __name__ == '__main__':
    unittest.main()
