#Imports
import unittest
from solution import is_int_palindrom


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_is_int_palindrom(self):

        self.assertTrue(True, is_int_palindrom(1))
        # True
        self.assertFalse(False, is_int_palindrom(42))
        # False
        self.assertTrue(True, is_int_palindrom(100001))
        # True
        self.assertTrue(True, is_int_palindrom(999))
        # True
        self.assertFalse(False, is_int_palindrom(123))
        # False


#Program Run
if __name__ == '__main__':
    unittest.main()
