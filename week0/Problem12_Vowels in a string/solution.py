def count_vowels(word):
    count = 0
    for i in word.lower():
        if i in "aeiouy":
            count += 1

    return count


def main():
    print(count_vowels("Python"))
    # 2
    print(count_vowels("Theistareykjarbunga"))
    # 8
    print(count_vowels("grrrrgh!"))
    # 0
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    # 22
    print(count_vowels("A nice day to code!"))
    # 8


if __name__ == '__main__':
    main()
