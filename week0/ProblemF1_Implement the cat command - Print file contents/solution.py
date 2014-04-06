# Imports
from sys import argv, exit

# Globals


# Function


# Main
def main():

    try:
        filename = argv[1]
    except IndexError:
        exit("Error: Argument not given!")

    try:
        filename = argv[1]
        fileOpen = open(filename, "r")
        content = fileOpen.read()
        print(content)
        fileOpen.close()

    except (IOError, IndexError):
        exit("Error: Try again, wrong file name!")

# Program run
if __name__ == "__main__":
    main()
