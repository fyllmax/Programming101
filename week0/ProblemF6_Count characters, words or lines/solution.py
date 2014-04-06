# Imports
from sys import argv, exit

# Globals


# Function


# Main
def main():
    if len(argv) != 3:
        exit("Invalid number of arguments")

    # count chars
    if argv[1] == "chars":
        charsCount = 0

        filename = argv[2]
        file = ""

        try:
            file = open(filename, "r")
        except IOError:
            exit("Error: File not found!")

        for line in file:
            line = line.strip()
            charsCount += len(line)

        print(charsCount)

    # count words
    elif argv[1] == "words":
        wordsList = []

        filename = argv[2]
        file = ""

        try:
            file = open(filename, "r")
        except IOError:
            exit("Error: File not found!")

        for line in file:
            line = line.rsplit()
            for word in line:
                wordsList.append(word)

        print(len(wordsList))

    # count lines
    elif argv[1] == "lines":
        numLines = 0

        filename = argv[2]
        file = ""

        try:
            file = open(filename, "r")
        except IOError:
            exit("Error: File not found!")

        for line in file:
            numLines += 1

        print(numLines)

    else:
        exit("Invalid command given")

# Program run
if __name__ == "__main__":
    main()
