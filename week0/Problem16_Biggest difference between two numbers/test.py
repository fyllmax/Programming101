# Imports
import unittest
from solution import biggest_difference


# Test

class test_smtg_test(unittest.TestCase):

    """Testing the unit"""

    def test_biggest_difference(self):

        self.assertEqual(-1, biggest_difference([1, 2]))
        # -1
        self.assertEqual(-4, biggest_difference([1, 2, 3, 4, 5]))
        # -4
        self.assertEqual(-9, biggest_difference([-10, -9, -1]))
        # -9
        self.assertEqual(-99, biggest_difference(range(100)))
        # -99


# Program Run
if __name__ == '__main__':
    unittest.main()
