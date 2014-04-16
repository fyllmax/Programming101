#Imports
import unittest
from entity import Entity, Hero, Orc, randint
from weapon import Weapon

#Test


class test_entity(unittest.TestCase):
    """Testing the unit"""

    def setUp(self):

        self.hero = Hero("Loki", 100, "The Nutcracker")
        self.entity = Entity("Avera", 999)
        self.orc = Orc("Ludia", 777, 3)

    def test_create_hero(self):
        self.assertEqual("Loki", self.hero.name)
        self.assertEqual(100, self.hero.health)
        self.assertEqual("The Nutcracker", self.hero.nickname)
        self.assertEqual(100, self.hero.max_health)
        self.assertTrue(True, self.hero.is_alive)
        self.assertFalse(False, self.hero.equipped_weapon)

    def test_hero_known_as(self):
        self.assertEqual("%s %s" % (self.hero.name, self.hero.nickname), self.hero.known_as())

    def test_create_entity(self):
        self.assertEqual("Avera", self.entity.name)
        self.assertEqual(999, self.entity.health)
        self.assertEqual(999, self.entity.max_health)
        self.assertTrue(True, self.entity.is_alive)
        self.assertFalse(False, self.entity.equipped_weapon)

    def test_entity_get_health(self):
        self.assertEqual(self.entity.health, self.entity.get_health())

    def test_hero_get_health(self):
        self.assertEqual(self.hero.health, self.hero.get_health())

    def test_entity_take_damage_more_then_health(self):
        self.entity.take_damage(randint(0, self.entity.max_health))
        self.assertEqual(self.entity.health, self.entity.get_health())

    def test_entity_take_damage_less_then_health(self):
        self.entity.take_damage(randint(0, self.entity.max_health))
        self.assertEqual(self.entity.health, self.entity.get_health())

    def test_hero_take_damage_more_then_health(self):
        self.hero.take_damage(randint(0, self.entity.max_health))
        self.assertEqual(self.hero.health, self.hero.get_health())

    def test_hero_take_damage_less_then_health(self):
        self.entity.take_damage(randint(0, self.entity.max_health))
        self.assertEqual(self.hero.health, self.hero.get_health())

    def test_entity_take_healng_when_alive(self):
        self.entity.is_alive = True
        expected = self.entity.take_healing(randint(0, self.entity.max_health))
        self.assertTrue(True, expected)

    def test_entity_take_healng_when_dead(self):
        self.entity.is_alive = False
        expected = self.entity.take_healing(randint(0, self.entity.max_health))
        self.assertFalse(False, expected)

    def test_has_weapon(self):
        self.assertFalse(False, self.entity.has_weapon())

    def test_equip_weapon(self):
        self.theFist = Weapon("The Anger Fist", 25, 0)
        self.entity.equip_weapon(self.theFist)
        self.assertTrue(True, self.entity.has_weapon())

    def test_attack_bare_hands(self):
        # self.entity.equipped_weapon = False
        self.assertEqual(0, self.entity.attack())

    def test_attack_with_weapon(self):
        self.theFist = Weapon("The Anger Fist", 1, 0)
        self.entity.equip_weapon(self.theFist)
        self.assertEqual(self.theFist.damage, self.entity.attack())

    def test_orc_attack_with_weapon(self):
        self.theFist = Weapon("The Anger Fist", 1, 0)
        self.orc.equip_weapon(self.theFist)
        self.assertEqual((self.theFist.damage * self.orc.berserk_factor), self.orc.attack())






#Program Run
if __name__ == '__main__':
    unittest.main()
