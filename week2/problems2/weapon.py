# Imports
from random import random

# Globals


# Function
class Weapon():

    """docstring for weapon"""

    def __init__(self, type, damage, critical_strike_percent):

        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        critical_chance = random()
        if critical_chance <= self.critical_strike_percent:
            return True
        else:
            return False
