from sys import argv, exit
from random import randint


def main():
    if len(argv) < 3:
        exit("Error: Not enough arguments given!")

    file_name = argv[1]
    numbers = int(argv[2])

    text_file = open(file_name, 'w+')

    for i in range(numbers):
        generated_numbers = (randint(1, numbers))
        text_file.write(str(generated_numbers))
        text_file.write(' ')
    text_file.close()

if __name__ == '__main__':
    main()
