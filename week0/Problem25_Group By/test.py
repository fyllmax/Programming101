#Imports
import unittest
from solution import groupby


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""
    def test_groupby(self):


        self.assertEqual({0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}, groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
        # {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        self.assertEqual({'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}, groupby(lambda x: 'odd' if x %
              2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
        # {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        self.assertEqual({0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}, groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
    # {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]


#Program Run
if __name__ == '__main__':
    unittest.main()
