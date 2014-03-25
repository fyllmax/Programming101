#Imports
import unittest
from solution import count_words


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_count_words(self):

        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(["apple", "banana", "apple", "pie"]))
# {'apple': 2, 'pie': 1, 'banana': 1}
        self.assertEqual({'ruby': 1, 'python': 3}, count_words(["python", "python", "python", "ruby"]))
# {'ruby': 1, 'python': 3}


#Program Run
if __name__ == '__main__':
    unittest.main()
