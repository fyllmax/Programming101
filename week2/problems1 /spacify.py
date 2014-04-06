from string_utils import tab_to_spaces
from sys import argv


def spacify(argv):

    f = open(argv[1], "r")
    content = f.read()
    new_content = tab_to_spaces(content, 4)
    f.close()

    f = open(argv[1], "w")
    f.write(new_content)
    f.close()


# main
def main():

    print(spacify(argv[1], 4))


# Program run
if __name__ == "__main__":
    main()
