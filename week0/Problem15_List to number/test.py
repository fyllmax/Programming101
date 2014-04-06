#Imports
import unittest
from solution import list_to_number


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_list_to_number(self):

        self.assertEqual(123, list_to_number([1, 2, 3]))
        # 123
        self.assertEqual(99999, list_to_number([9, 9, 9, 9, 9]))
        # 99999
        self.assertEqual(123023, list_to_number([1, 2, 3, 0, 2, 3]))
        # 123023


#Program Run
if __name__ == '__main__':
    unittest.main()
