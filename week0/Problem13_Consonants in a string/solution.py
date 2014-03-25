def count_consonants(word):
    count = 0
    for i in word.lower():
        if i in "bcdfghjklmnpqrstvwxz":
            count += 1

    return count


def main():
    print(count_consonants("Python"))
    # 4
    print(count_consonants("Theistareykjarbunga"))
    # 11
    print(count_consonants("grrrrgh!"))
    # 7
    print(count_consonants("Github is the second best thing \
            that happend to programmers, after the keyboard!"))
    # 44
    print(count_consonants("A nice day to code!"))
    # 6
if __name__ == '__main__':
    main()
