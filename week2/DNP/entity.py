#Imports
from random import randint
from weapon import Weapon

#Globals


#Function
class Entity():
    """docstring for Entity"""
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.alive = True
        self.equipped_weapon = False
        self.attack_damage = 0
        self.critical_hit = 1

    def is_alive(self):
        if self.health < 1:
            self.heath = 0
            self.alive = False
            return False

        self.alive = True
        return True

    def get_health(self):
        return self.health

    def take_damage(self, damage_points):

        # damage_points = randint(0, self.max_health)

        if self.health <= damage_points:
            self.health = 0

        else:
            self.health -= damage_points

        return self.health

    def take_healing(self, healing_points):

        # healing_points = randint(0, self.max_health)

        healed = False

        if healing_points >= self.max_health - self.health and self.is_alive:
            healing_points -= (self.max_health - self.health)
            self.health += healing_points
            healed = True

        elif healing_points <= self.max_health - self.health and self.is_alive:
            self.health += healing_points
            healed = True

        else:
            healed

        return healed

    def has_weapon(self):

        return self.equipped_weapon

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.attack_damage = self.weapon.damage
        self.equipped_weapon = True

    def attack(self):

        if not self.equipped_weapon:
            self.critical_hit = 1

        else:
            if self.weapon.critical_hit():
                self.critical_hit = 2

        return self.attack_damage * self.critical_hit


class Hero(Entity):
    """docstring for Hero"""
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname
        self.race = "Hero"

    def known_as(self):
        return ("{} {}".format(self.name, self.nickname))


class Orc(Entity):
    """docstring for Orc"""
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor
        self.race = "Orc"

        if self.berserk_factor > 2:
            self.berserk_factor = 2
        else:
            self.berserk_factor = 1

    def attack(self):

        if not self.equipped_weapon:
            self.critical_hit = 1

        else:
            if self.weapon.critical_hit():
                self.critical_hit = 2

        return self.attack_damage * self.critical_hit * self.berserk_factor


#Main


# def main():
#     loki = Hero("Avera", 100, "The Nutcracker")
#     loki.take_damage(150)
#     print(loki.get_health())

# #Program run
# if __name__ == '__main__':
#     main()
