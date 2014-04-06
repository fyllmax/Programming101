#Imports
import unittest
from solution import number_to_list


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_number_to_list(self):

        self.assertEqual([1, 2, 3], number_to_list(123))
        # [1, 2, 3]
        self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))
        # [9, 9, 9, 9, 9]
        self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))
        # [1, 2, 3, 0, 2, 3]


#Program Run
if __name__ == '__main__':
    unittest.main()
