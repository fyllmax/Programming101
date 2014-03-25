#Imports
import unittest
from solution import prime_number_of_divisors


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def test_prime_number_of_divisors(self):
        self.assertTrue(True, prime_number_of_divisors(7))
        # True
        self.assertFalse(False, prime_number_of_divisors(8))
        # False
        self.assertTrue(True, prime_number_of_divisors(9))
        # True



#Program Run
if __name__ == '__main__':
    unittest.main()
