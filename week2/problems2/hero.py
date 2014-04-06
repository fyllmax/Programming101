# Imports
from random import randint

# Globals


# Function
class Hero():

    """docstring for ClassName"""

    def __init__(self, name, health, nickname):
        self.name = name
        self.health = health
        self.nickname = nickname
        self.is_alive = True

    def known_as(self):
        print("%s %s" % (self.name, self.nickname))

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return self.is_alive

        elif self.health == 0:
            self.is_alive = False
            return self.is_alive

    def take_damage(self):
        self.damage_points = randint(0, 101)
        self.health -= self.damage_points

    def take_healing(self):
        max_health = 0

        if self.health == 0:
            print("too late for healing")
            return False
        elif self.health > 0:
            max_health = 100 - self.health
            self.healing_points = randint(0, max_health)

new_hero = Hero("BashMaistora", 100, "HipMunk Beast")
