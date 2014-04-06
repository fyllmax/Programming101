#Imports
import unittest
from solution import is_prime


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_is_prime(self):
        self.assertTrue(True, is_prime(11))
        # True
        self.assertFalse(False, is_prime(1))
        # False
        self.assertTrue(True, is_prime(2))
        # True
        self.assertFalse(False, is_prime(8))
        # False
        self.assertTrue(True, is_prime(11))
        # True
        self.assertFalse(False, is_prime(-10))
        # False


#Program Run
if __name__ == '__main__':
    unittest.main()
