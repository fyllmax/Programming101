#Imports
import unittest
from fight import Fight
from entity import Hero, Orc
from weapon import Weapon


#Test

class test_fight(unittest.TestCase):
    """Testing the unit"""

    def setUp(self):

        self.hero = Hero("Linux", 100, "Luna OS")
        self.orc = Orc("Mac OS", 100, 1)

        TheFist = Weapon("Anger Fist", 35, 0.3)
        self.hero.equip_weapon(TheFist)

        TheBlades = Weapon("Ilidan Blades", 20, 0.25)
        self.orc.equip_weapon(TheBlades)

        self.fight = Fight(self.hero, self.orc)

    def test_attack_first(self):

        if self.fight.attack_first == self.hero.name:
            self.assertEqual(self.hero.name, self.fight.attack_first)
        else:
            self.assertEqual(self.orc.name, self.fight.attack_first)

    # def test_stimulate_fight(self):
    #     self.assertTrue(self.fight.simulate_fight())


#Program Run
if __name__ == '__main__':
    unittest.main()
