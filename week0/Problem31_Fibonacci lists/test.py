#Imports
import unittest
from solution import nth_fib_lists


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_nth_fib_lists(self):

        self.assertEqual([1], nth_fib_lists([1], [2], 1))
        # [1]
        self.assertEqual([2], nth_fib_lists([1], [2], 2))
        # [2]
        self.assertEqual([1, 2, 1, 3], nth_fib_lists([1, 2], [1, 3], 3))
        # [1, 2, 1, 3]
        self.assertEqual([1, 2, 3, 1, 2, 3], nth_fib_lists([], [1, 2, 3], 4))
        # [1, 2, 3, 1, 2, 3]
        self.assertEqual([], nth_fib_lists([], [], 100))
        # []


#Program Run
if __name__ == '__main__':
    unittest.main()
