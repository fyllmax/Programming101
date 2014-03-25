from sys import argv
import re

def lines(text):
    return text.split("\n")


def unlines(elements):
    return "\n".join(elements)


def words(text):
    return text.split()


def unword(elements):
    return " ".join(elements)


def tab_to_spaces(text, tab):
    return re.sub('[ \t]+', tab*" ", text)
    


# main
def main():

    lines("new\ntest")
    lines("last\ntest")

    print(unlines(["hello", "world"]))
    print(unlines(["new", "test"]))

    words("hello world")
    words("new test")

    unword("hello world hello dolly")
    unword("new test fuck yahh")



# Program run
if __name__ == "__main__":
    main()
