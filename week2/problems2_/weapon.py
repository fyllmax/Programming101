#Imports
from random import random

#Globals


#Function


class Weapon():
    """docstring for Weapon"""
    def __init__(self, model, damage, critical_strike_percent):

        self.model = model

        self.damage = damage
        if self.damage < 1:
            self.damage = 1

        self.critical_strike_percent = critical_strike_percent
        if self.critical_strike_percent > 1:
            self.critical_strike_percent = 1
        elif self.critical_strike_percent < 0:
            self.critical_strike_percent = 0

    def critical_hit(self):

        critical_chance = random()

        if critical_chance <= self.critical_strike_percent:
            return True
        else:
            return False
