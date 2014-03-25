# Imports
from sys import argv

# Globals


# Function
def map_dungeon(argv):
    map_dng = argv[1]
    OpenMap = open(map_dng, "r")
    content = OpenMap.read()
    print(content)

# Main


def main():
    print(map_dungeon(argv))


# Program run
if __name__ == "__main__":
    main()
