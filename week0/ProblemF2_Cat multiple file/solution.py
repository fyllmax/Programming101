#Imports
from sys import argv, exit

#Globals


#Function


#Main
def main():
    if len(argv) <= 1:
        exit("Did you give any arguments")

    try:
        for i in range(1, len(argv)):
            filename = argv[i]
            fileOpen = open(filename, "r")
            content = fileOpen.read()
            print(content)
            fileOpen.close()

    except (IOError, IndexError):
        exit("Error: check your file name|arguments!")


#Program run
if __name__ == "__main__":
    main()
