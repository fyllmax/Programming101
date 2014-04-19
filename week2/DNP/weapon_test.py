#Imports
import unittest
from weapon import Weapon


#Test

class test_weapon(unittest.TestCase):
    """Testing the unit"""
    def setUp(self):
        self.weapon = Weapon("The Anger Fist", 25, 0.3)

    def test_creating_weapon(self):
        self.assertEqual("The Anger Fist", self.weapon.model)
        self.assertEqual(25, self.weapon.damage)
        self.assertEqual(0.3, self.weapon.critical_strike_percent)


#Program Run
if __name__ == '__main__':
    unittest.main()
