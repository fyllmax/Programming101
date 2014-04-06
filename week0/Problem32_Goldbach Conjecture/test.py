# Imports
import unittest
from solution import goldbach
# Test


class test_smtg_test(unittest.TestCase):

    """Testing the unit"""

    def test_goldbach(self):

        self.assertEqual([(2, 2)], goldbach(4))
        # [(2,2)]
        self.assertEqual([(3, 3)], goldbach(6))
        # [(3,3)]
        self.assertEqual([(3, 5)], goldbach(8))
        # [(3,5)]
        self.assertEqual([(3, 7), (5, 5)], goldbach(10))
        # [(3,7), (5,5)]
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71),
                         (41, 59), (47, 53)], goldbach(100))
        # [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53 )]

# Program Run
if __name__ == '__main__':
    unittest.main()
