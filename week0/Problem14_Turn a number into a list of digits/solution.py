def number_to_list(n):
    to_str = str(n)
    to_list = list(to_str)
    return [int(x) for x in to_list]


def main():
    print(number_to_list(123))
    # [1, 2, 3]
    print(number_to_list(99999))
    # [9, 9, 9, 9, 9]
    print(number_to_list(123023))
    # [1, 2, 3, 0, 2, 3]

if __name__ == '__main__':
    main()
