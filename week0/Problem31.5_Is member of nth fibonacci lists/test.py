# Imports
import unittest
from solution import member_of_nth_fib_lists


# Test

class test_smtg_test(unittest.TestCase):

    """Testing the unit"""

    def test_member_of_nth_fib_lists(self):

        self.assertFalse(False, member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
        # False
        self.assertTrue(True, member_of_nth_fib_lists([1, 2],
                                                      [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
        # True
        self.assertTrue(
            True, member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
        # True
        self.assertFalse(
            False, member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))
        # False


# Program Run
if __name__ == '__main__':
    unittest.main()
