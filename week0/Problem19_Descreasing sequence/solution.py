def is_decreasing(seq):
    x = False

    for i in range(len(seq) - 1):

        if seq[i] > seq[i + 1]:
            x = True
        else:
            x = False
            return x
    return x


def main():

    print(is_decreasing([5, 4, 3, 2, 1]))
    # True
    print(is_decreasing([1, 2, 3]))
    # False
    print(is_decreasing([100, 50, 20]))
    # True
    print(is_decreasing([1, 1, 1, 1]))
    # False

if __name__ == '__main__':
    main()
