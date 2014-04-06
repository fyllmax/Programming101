def unique_words_count(arr):

    dict = {}

    for i in arr:
        dict[i] = arr.count(i)

    return len(dict)


def main():

    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    # 3
    print(unique_words_count(["python", "python", "python", "ruby"]))
    # 2
    print(unique_words_count(["HELLO!"] * 10))
    # 1

if __name__ == '__main__':
    main()
