# Imports
from random import randint
from weapon import Weapon

# Globals


# Function
class Entity():

    """docstring for ClassName"""

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.is_alive = True
        self.max_health = health
        self.equppted_weapon = False

    def known_as(self):
        print("%s %s" % (self.name, self.nickname))
        return ("%s %s" % (self.name, self.nickname))

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return self.is_alive

        elif self.health == 0:
            self.is_alive = False
            return self.is_alive

    def take_damage(self, damage_points):
        damage_points = randint(0, 101)
        self.health -= damage_points
        if self.health < damage_points:
            self.healing_points = 0
            self.is_alive = False

    def take_healing(self, healing_points):

        healing_points = randint(0, self.max_health)

        if not self.is_alive:
            print("too late for healing")
            return False

        else:
            max_health = self.max_health - self.health
            healing_points = randint(0, max_health)
            self.health += healing_points
            print("Healing is successful")
            return True

    def has_weapon(self):
        if self.equipped_weapon:
            return True
        else:
            return False

    def equip_weapon(self, weapon):
        if not self.equppted_weapon:
            self.equppted_weapon = weapon
        else:
            self.equppted_weapon = weapon

    def attack(self):
        if not self.equppted_weapon:
            return 0
        elif Weapon.critical_hit:
            return Weapon.damage * 2


class Hero(Entity):

    """docstring for ClassName"""

    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname


class Orc(Entity):

    """docstring for ClassName"""

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor
        if self.berserk_factor > 2:
            self.berserk_factor = 2
        else:
            self.berserk_factor = 1

        def attack(self):
            if not self.equppted_weapon:
                return 0
            else:
                return Weapon.damage * self.berserk_factor
