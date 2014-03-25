# Imports
import unittest
from solution import prepare_meal


# Test

class test_smtg_test(unittest.TestCase):

    """Testing the unit"""

    def test_prepare_meal(self):

        self.assertEqual('eggs', prepare_meal(5))
        # 'eggs'
        self.assertEqual('spam and eggs', prepare_meal(15))
        # 'spam and eggs'
        self.assertEqual('spam spam and eggs', prepare_meal(45))
        # 'spam spam and eggs'
        self.assertEqual('spam', prepare_meal(3))
        # "spam"
        self.assertEqual("spam spam spam", prepare_meal(27))
        # "spam spam spam"
        self.assertEqual("", prepare_meal(7))
        # ""


# Program Run
if __name__ == '__main__':
    unittest.main()
