#Imports
import unittest
from solution import sum_of_min_and_max


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_sum_of_min_and_max(self):

        self.assertEqual(10, sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]))
        # 10
        self.assertEqual(90, sum_of_min_and_max([-10, 5, 10, 100]))
        # 90
        self.assertEqual(2, sum_of_min_and_max([1]))
        # 2

#Program Run
if __name__ == '__main__':
    unittest.main()
