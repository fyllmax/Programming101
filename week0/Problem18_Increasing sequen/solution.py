def is_increasing(seq):
    x = False

    if len(seq) == 1:
        return True

    for i in range(len(seq) - 1):

        if seq[i] < seq[i + 1]:
            x = True
        else:
            x = False
            return x
    return x


def main():
    print(is_increasing([1, 2, 3, 4, 5]))
    # True
    print(is_increasing([1]))
    # True
    print(is_increasing([5, 6, -10]))
    # False
    print(is_increasing([1, 1, 1, 1]))
    # False

if __name__ == '__main__':
    main()
