#Imports
import unittest
from solution import unique_words_count


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""
    def test_unique_words_count(self):

        self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))
        # 3
        self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))
        # 2
        self.assertEqual(1, unique_words_count(["HELLO!"] * 10))
        # 1


#Program Run
if __name__ == '__main__':
    unittest.main()
