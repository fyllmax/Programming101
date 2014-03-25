#Imports
from sys import argv, exit

#Globals


#Function


#Main
def main():
    if len(argv) == 1:
        exit("Invalid number of arguments")

    MEGATRON = open("MEGATRON.txt", "w")

    for i in range(1, len(argv)):
        filename = argv[i]
        file = ""
        try:
            file = open(filename, "r")
        except IOError:
            exit("Error: File not found!")
        content = file.read()
        MEGATRON.write(content)
        MEGATRON.write("\n")

#Program run
if __name__ == "__main__":
    main()
