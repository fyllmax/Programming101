# Imports
from dungeon import Dungeon
from fight import Fight
from entity import Hero, Orc
from weapon import Weapon
from random import randint


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
            self.player1 = Orc(player_name, 100, 2)

            print('')
            print("{} is equiped with:".format(player_name))

            self.player1.equip_weapon(self.give_weapon())

        else:
            self.entity = "H"
            self.player2 = Hero(player_name, 100, "The NutCracker")

            print('')
            print("{} is equiped with:".format(player_name))

            self.player2.equip_weapon(self.give_weapon())

        for i in range(len(self.dungeon_map)):
            for j in range(len(self.dungeon_map[i])):
                if self.dungeon_map[i][j] == "S":
                    self.dungeon_map[i][j] = self.entity
                    self.cords.setdefault(self.player_name, []).append(i)
                    self.cords.setdefault(self.player_name, []).append(j)
                    return True
        return False

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

        # print('{} is on cords {}'.format(name, self.cords[name]))
        self.fight_time()
        return True

    def get_cords(self, name):
        return self.cords[name]

    def fight_time(self):
        if self.cords[self.spawned[0]] == self.cords[self.spawned[1]]:
            print('')
            print("Its time for fight. Lets Bet!")
            print('')
            self.its_show_time = Fight(self.player1, self.player2)
            self.its_show_time.simulate_fight()

    def give_weapon(self):

        TheFist = Weapon("Anger Fist", 35, 0.3)

        TheBlades = Weapon("Ilidan Blades", 20, 0.25)

        GladiatorKnife = Weapon("Axill Sword", 15, 0.5)

        TheRebornMace = Weapon("Trojan Mace", 50, 0.15)

        ThunderKick = Weapon("Chuck Noriss Right Leg", 80, 1)

        PitLord = Weapon("Black Hole", 50, 0.1)

        Ruthless = Weapon("Bitch Slap", 45, 0.4)

        select_weapon = randint(0, 6)

        weapons = [TheFist, TheBlades, GladiatorKnife, TheRebornMace, ThunderKick, PitLord, Ruthless]

        print(weapons[select_weapon].model)
        return weapons[select_weapon]


# def main():

#     new_map = Dungeon('basic_dungeon.txt')
#     map_play = Map(new_map)
#     map_play.spawn('Loki', 'orc')
#     map_play.spawn('Arthur', 'hero')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'down')
#     map_play.move('Loki', 'down')
#     map_play.move('Loki', 'down')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'up')
#     map_play.move('Loki', 'up')
#     map_play.move('Loki', 'up')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'right')
#     map_play.move('Loki', 'down')
#     map_play.move('Loki', 'down')
#     map_play.move('Loki', 'down')
#     map_play.move('Loki', 'down')


# if __name__ == '__main__':
#     main()
