# Imports
# from sys import argv


# Globals


# Function
class Dungeon():

    """docstring for Dungeon"""

    def __init__(self, map_file):
        self.map_file = open(map_file, "r")
        self.map_content = self.map_file.read()
        self.map_file.close()
        self.dng_to_matrix = self.map_content.split("\n")
        for i in range(len(self.dng_to_matrix)):
            self.dng_to_matrix[i] = list(self.dng_to_matrix[i])

    def print_map(self):
        # print(self.map_content, "\n")
        print(self.dng_to_matrix)
        return self.dng_to_matrix

    def Spawn(self, player_name, entity):
        self.player_name = player_name
        self.entity = entity
        self.cords = []

        if self.entity == "Orc":
            self.entity = "O"
        else:
            self.entity = "H"

        for i in range(len(self.dng_to_matrix)):
            for j in range(len(self.dng_to_matrix[i])):
                if self.dng_to_matrix[i][j] == "S":
                    i[j] = self.entity
                    self.cords.append(i)
                    self.cords.append(i[j])
                    print(self.dng_to_matrix)
                    return True
                else:
                    return False

    def move(self, player_name, direction):
        self.max_path = len(self.dng_to_matrix) - 1
        self.UpDown = self.cords[0]
        self.LeftRight = self.cords[1]
        self.position = x[self.UpDown][self.LeftRight]

        if direction == "right" and x[UpDown][LeftRight + 1] != "o" and 0 < LeftRight < max_path:

            LeftRight += 1
            position = x[UpDown][LeftRight]
            print("possition updated")


        elif direction == "left" and x[UpDown][LeftRight - 1] != "o" and 0 < LeftRight < max_path:

            position = x[UpDown][LeftRight - 1]
            LeftRight -= 1
            print("possition updated")

        elif direction == "up" and x[UpDown - 1][LeftRight] != "o" and 0 < UpDown < max_path:
            UpDown -= 1
            position = x[UpDown][LeftRight]
            print("possition updated")


        elif direction == "down" and x[UpDown + 1][LeftRight] != "o" and 0 < UpDown < max_path:
            UpDown += 1
            position = x[UpDown][LeftRight]
            print("possition updated")

        else:
            print("illigal move, try different direction")

        return position


# Main
def main():
    map_dng = Dungeon("basic_dungeon.txt")
    map_dng.Spawn("Odyssey", "Orc")
    map_dng.Spawn("Asparuh", "Hero")

if __name__ == '__main__':
    main()
