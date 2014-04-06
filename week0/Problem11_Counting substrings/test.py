# Imports
import unittest
from solution import count_substrings


# Test

class test_smtg_test(unittest.TestCase):

    """Testing the unit"""

    def test_count_substrings(self):
        self.assertEqual(2, count_substrings("This is a test string", "is"))
    # 2
        self.assertEqual(2, count_substrings("babababa", "baba"))
        # 2
        self.assertEqual(
            4, count_substrings("Python is an awesome language to program in!", "o"))
        # 4
        self.assertEqual(
            0, count_substrings("We have nothing in common!", "really?"))
        # 0
        self.assertEqual(
            2, count_substrings("This is this and that is this", "this"))
        # 2


# Program Run
if __name__ == '__main__':
    unittest.main()
