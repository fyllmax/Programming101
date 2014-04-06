def count_words(arr):

    dict = {}

    for i in arr:
        dict[i] = arr.count(i)

    return dict


def main():

    print(count_words(["apple", "banana", "apple", "pie"]))
    # {'apple': 2, 'pie': 1, 'banana': 1}
    print(count_words(["python", "python", "python", "ruby"]))
    # {'ruby': 1, 'python': 3}

if __name__ == '__main__':
    main()
