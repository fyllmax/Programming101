#Imports
import unittest
from solution import count_consonants


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_count_consonants(self):

        self.assertEqual(4, count_consonants("Python"))
        # 4
        self.assertEqual(11, count_consonants("Theistareykjarbunga"))
        # 11
        self.assertEqual(7, count_consonants("grrrrgh!"))
        # 7
        self.assertEqual(44, count_consonants("Github is the second best thing \
        that happend to programmers, after the keyboard!"))
        # 44
        self.assertEqual(6, count_consonants("A nice day to code!"))
        # 6

#Program Run
if __name__ == '__main__':
    unittest.main()
