#Imports
import unittest
from solution import count_vowels


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""
    def test_count_vowels(self):
        self.assertEqual(2, count_vowels("Python"))
        # 2
        self.assertEqual(8, count_vowels("Theistareykjarbunga"))
        # 8
        self.assertEqual(0, count_vowels("grrrrgh!"))
        # 0
        self.assertEqual(22, count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
        # 22
        self.assertEqual(8, count_vowels("A nice day to code!"))
        # 8


#Program Run
if __name__ == '__main__':
    unittest.main()
