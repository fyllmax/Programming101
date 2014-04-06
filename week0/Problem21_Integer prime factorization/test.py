#Imports
import unittest
from solution import prime_factorization


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_prime_factorization(self):

        self.assertEqual({2: 1, 5: 1}, prime_factorization(10))
        # {2: 1, 5, 1} # This is 2^1 * 5^1
        self.assertEqual({2: 1, 7: 1}, prime_factorization(14))

        self.assertEqual({2: 2, 89: 1}, prime_factorization(356))
        # [(2, 2), (89, 1)]
        self.assertEqual({89: 1}, prime_factorization(89))
        # {8:, ) # 89}  a prime number
        self.assertEqual({2: 3, 5: 3}, prime_factorization(1000))
        # {2: 3, 5, 3}

#Program Run
if __name__ == '__main__':
    unittest.main()
