#Imports
from sys import argv, exit

#Globals


#Function


#Main
def main():

    if len(argv) == 1 or len(argv) > 2:
        exit("Error: check arguments again!")

    file_name = argv[1]
    total = 0
    try:
        text_file = open(file_name, "r")
    except IOError:
        exit("Error: File not found!")
    text_list = text_file.read()
    text_list = text_list.split()
    for i in text_list:
        total += int(i)

    print(total)
    text_file.close()


#Program run
if __name__ == "__main__":
    main()
