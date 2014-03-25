#Imports
import unittest
from solution import sum_of_divisors

#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_sum_of_divisors(self):

        self.assertEqual(15, sum_of_divisors(8))
        # 15
        self.assertEqual(8, sum_of_divisors(7))
        # 8
        self.assertEqual(1, sum_of_divisors(1))
        # 1
        self.assertEqual(2340, sum_of_divisors(1000))
    # 2340

#Program Run
if __name__ == '__main__':
    unittest.main()
