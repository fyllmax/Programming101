from weapon import Weapon
from random import randint


def give_weapon():

    TheFist = Weapon("Anger Fist", 35, 0.3)

    TheBlades = Weapon("Ilidan Blades", 20, 0.25)

    GladiatorKnife = Weapon("Axill Sword", 15, 0.5)

    TheRebornMace = Weapon("Trojan Mace", 50, 0.15)

    ThunderKick = Weapon("Chuck Noriss Enlightment", 80, 1)

    PitLord = Weapon("Black Hole", 50, 0.1)

    Ruthless = Weapon("Bitch Slap", 45, 0.4)

    select_weapon = randint(0, 6)

    weapons = [TheFist, TheBlades, GladiatorKnife, TheRebornMace, ThunderKick, PitLord, Ruthless]

    print(weapons[select_weapon].model)
    return weapons[select_weapon]
