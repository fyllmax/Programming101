# Imports
from dungeon import Dungeon
from fight import Fight
from entity import Hero, Orc
from weapon import Weapon
from random import randint
from snakes import Python
from snakes import Anaconda
from item import give_weapon


class Map():
    """docstring for Map"""
    def __init__(self, dng_map):

        self.dng_map = dng_map
        self.dungeon_map = self.dng_map.map_to_matrix()
        self.max_path_UpDown = len(self.dungeon_map) - 1
        self.max_path_LeftRight = len(self.dungeon_map[0]) - 1
        self.cords = {}
        self.spawned = []

    def spawn(self, player_name, entity):

        self.player_name = player_name
        self.entity = entity.lower()
        self.spawned.append(self.player_name)

        if self.entity == "orc":
            self.entity = "O"
            self.player1 = Orc(player_name, 1000, 2)

            print('')
            print("{} is fighting with:".format(player_name))

            self.player1.equip_weapon(give_weapon())

        else:
            self.entity = "H"
            self.player1 = Hero(player_name, 1000, "The NutCracker")

            print('')
            print("{} is fighting with:".format(player_name))

            self.player1.equip_weapon(give_weapon())

        for i in range(len(self.dungeon_map)):
            for j in range(len(self.dungeon_map[i])):
                if self.dungeon_map[i][j] == "S":
                    self.dungeon_map[i][j] = self.entity
                    self.cords.setdefault(self.player_name, []).append(i)
                    self.cords.setdefault(self.player_name, []).append(j)
                    return True
        return False

    def get_cords(self, name):
        return '{} is on cords {}'.format(name, self.cords[name])

    def move(self, name, direction):
        self.UpDown = self.cords[name][0]
        self.LeftRight = self.cords[name][1]

        if direction == "right" and self.dungeon_map[self.UpDown][self.LeftRight + 1] != "#" and 0 <= self.LeftRight <= self.max_path_LeftRight:

            self.LeftRight += 1
            self.cords[name][1] = self.LeftRight
            # print("position updated")

        elif direction == "left" and self.dungeon_map[self.UpDown][self.LeftRight - 1] != "#" and 0 <= self.LeftRight <= self.max_path_LeftRight:

            self.LeftRight -= 1
            self.cords[name][1] = self.LeftRight
            # print("position updated")

        elif direction == "up" and self.dungeon_map[self.UpDown - 1][self.LeftRight] != "#" and 0 <= self.UpDown <= self.max_path_UpDown:

            self.UpDown -= 1
            self.cords[name][0] = self.UpDown
            # print("position updated")

        elif direction == "down" and self.dungeon_map[self.UpDown + 1][self.LeftRight] != "#" and 0 <= self.UpDown <= self.max_path_UpDown:

            self.UpDown += 1
            self.cords[name][0] = self.UpDown
            # print("position updated")

        else:
            print("Illigal move")
            return False

        # print(self.get_cords(name))
        self.fight_time()

        return True

    def fight_time(self):

        if self.dungeon_map[self.UpDown][self.LeftRight] == 'P':
            print('')
            print("Its time for fight. Lets Bet!")
            print('')

            self.enemy = Python(10)

            self.its_show_time = Fight(self.player1, self.enemy)
            self.its_show_time.simulate_fight()

        elif self.dungeon_map[self.UpDown][self.LeftRight] == 'A':
            print('')
            print("Its time for fight. Lets Bet!")
            print('')

            self.enemy = Anaconda(10, (4, 1.5))

            self.its_show_time = Fight(self.player1, self.enemy)
            self.its_show_time.simulate_fight()

    def item(self):

        item = randint(0, 1)

        if self.dungeon_map[self.UpDown][self.LeftRight] == 'I':

            if item == 0:

                self.player1.equip_weapon(give_weapon())

            else:
                self.player1.take_healing()


def main():

    igrach = Dungeon(1)
    test = Map(igrach)

    test.spawn("Max", 'Orc')
    test.move("Max", 'right')
    test.move("Max", 'right')
    test.move("Max", 'right')


if __name__ == '__main__':
    main()
