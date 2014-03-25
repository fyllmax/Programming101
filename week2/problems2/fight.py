# Imports
import Entity
from random import randint
from weapon import Weapon
# Globals


# Function
class Fight(Entity):

    """docstring for ClassName"""

    def __init__(self, Hero, Orc):
        super().__init__(Hero, Orc)
        self.Hero = Hero
        self.Orc = Orc
        first_hit = randint(0, 100)

        if first_hit < 50:
            # weapon("The NutCracker", 20, 0.15)
            Hero.attack()

        else:
            # weapon("Thor Hammer ", 25, 0.07)
            Orc.attack()
            pass

            # Orc attacks first

    def simulate_fight(self):
