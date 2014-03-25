# Imports
import unittest
from solution import is_an_bn


# Test

class test_smtg_test(unittest.TestCase):

    """Testing the unit"""

    def test_is_an_bn(self):

        self.assertTrue(True, is_an_bn(""))
        # True
        self.assertFalse(False, is_an_bn("rado"))
        # False
        self.assertFalse(False, is_an_bn("aaabb"))
        # False
        self.assertTrue(True, is_an_bn("aaabbb"))
        # True
        self.assertFalse(False, is_an_bn("aabbaabb"))
        # False
        self.assertFalse(False, is_an_bn("bbbaaa"))
        # False
        self.assertTrue(True, is_an_bn("aaaaabbbbb"))
        # True


# Program Run
if __name__ == '__main__':
    unittest.main()
