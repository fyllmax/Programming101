#Imports
# from entity import Hero, Orc
# from weapon import Weapon
from random import randint


#Globals


#Function


class Fight():
    """docstring for Fight"""
    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2
        self.player1_name = self.player1.name
        self.player2_name = self.player2.name

        self.decide_first = randint(0, 100)
        self.attack_first = ""

        if self.decide_first < 50:
            self.attack_first = self.player1_name
        else:
            self.attack_first = self.player1_name

    def simulate_fight(self):

        if self.attack_first == self.player1_name:
            self.player2.take_damage(self.player1.attack())

        else:
            self.player1.take_damage(self.player2.attack())

        while True:
            attack_turn = randint(0, 100)

            if attack_turn < 50:
                damage = self.player1.attack()
                print("{} attacks for {}".format(self.player1.name, damage))
                self.player2.take_damage(damage)

            else:
                damage = self.player2.attack()
                print("{} attacks for {}".format(self.player2.name, damage))
                self.player1.take_damage(damage)

            if self.player1.is_alive() is False:
                print('')
                print("{} slapped badly {}".format(self.player1_name, self.player2_name))
                print('')
                break

            elif self.player2.is_alive() is False:
                print('')
                print("{} slapped badly {}".format(self.player2_name, self.player1_name))
                print('')
                break

        return True

#Main


# def main():

#         hero = Hero("Linux", 100, "Luna OS")
#         orc = Orc("Mac OS", 100, 1)

#         TheFist = Weapon("Anger Fist", 35, 0.3)
#         hero.equip_weapon(TheFist)

#         TheBlades = Weapon("Ilidan Blades", 20, 0.25)
#         orc.equip_weapon(TheBlades)
#         fight = Fight(hero, orc)
#         fight.simulate_fight()

# #Program run
# if __name__ == "__main__":
#     main()
