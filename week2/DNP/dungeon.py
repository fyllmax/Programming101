# Imports
from os import getcwd

# Function


class Dungeon():
    """docstring for Dungeon"""
    def __init__(self, level=1):

        self.level = level
        self.dng_map = self.map_to_matrix()

    def load_map(self):

        filename = getcwd() + '/maps/level_{}.txt'.format(str(self.level))

        try:
            fileOpen = open(filename, "r")
            self.content = fileOpen.read()
            fileOpen.close()

        except (IOError, IndexError):
            exit("Error: Try again, wrong file name given!")

        return self.content

    def map_to_matrix(self):
        str_map = self.load_map().split('\n')
        matrix_map = []
        for i in range(len(str_map)):
            matrix_map.append(list(str_map[i]))
        return matrix_map

    def print_map(self):
        return self.map_to_matrix()


# def main():
#     test = Dungeon(2)
#     print(test.load_map())
#     print(test.print_map())
# if __name__ == '__main__':
#     main()
