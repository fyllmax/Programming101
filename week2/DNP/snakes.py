from entity import Entity
from random import randint


class Python(Entity):
    def __init__(self, health):
        super().__init__(self, health)
        self.name = 'Nasty Python'

    def attack(self):
        return randint(1, 5)


class Anaconda(Python):
    """docstring for Orc"""
    def __init__(self, health, berserk_factor):
        super().__init__(health)

        self.name = 'GAD Anaconda'
        self.damage = randint(15, 45)
        self.berserk_factor = berserk_factor
        self.prior_berserk_attack = self.berserk_factor[0]
        self.berserk_attack = self.berserk_factor[1]
        self.count_hits = 0

    def attack(self):

        self.count_hits += 1

        if self.attack_count < self.prior_berserk_attack:
            return self.damage

        elif self.attack_count == self.prior_berserk_attack:
            self.attack_count = 0
            return self.damage * self.berserk_attack

        else:
            return False


# def main():
#     test = Anaconda(10000, (4, 1.5))
#     print(test.get_health())
#     print(test.name)

# if __name__ == '__main__':
#     main()
