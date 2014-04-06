#Imports
import unittest
from solution import sort_fractions


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_sort_fractions(self):

        self.assertEqual([(1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2)]))
        self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2), (1, 3)]))
#Program Run
if __name__ == '__main__':
    unittest.main()
