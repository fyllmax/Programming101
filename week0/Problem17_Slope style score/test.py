#Imports
import unittest
from solution import slope_style_score


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""
    def test_slope_style_score(self):

        self.assertEqual(94.67, slope_style_score([94, 95, 95, 95, 90]))
        # 94.66
        self.assertEqual(80.0, slope_style_score([60, 70, 80, 90, 100]))
        # 80.0
        self.assertEqual(93.5, slope_style_score([96, 95.5, 93, 89, 92]))
        # 93.5


#Program Run
if __name__ == '__main__':
    unittest.main()
