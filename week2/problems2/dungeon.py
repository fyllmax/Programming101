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

    def print_map(self):
        print(self.map_content)
        return self.map_content


# Main
def main():
    map_dng = Dungeon("basic_dungeon.txt")
    map_dng.print_map()

if __name__ == '__main__':
    main()
