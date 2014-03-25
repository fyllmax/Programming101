#Imports
import unittest
from solution import sevens_in_a_row


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_sevens_in_a_row(self):
        self.assertTrue(True, sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
        # True
        self.assertFalse(False, sevens_in_a_row([1, 7, 1, 7, 7], 4))
        # False
        self.assertTrue(True, sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
        # True
        self.assertTrue(True, sevens_in_a_row([7, 2, 1, 6, 2], 1))
        # True

#Program Run
if __name__ == '__main__':
    unittest.main()
