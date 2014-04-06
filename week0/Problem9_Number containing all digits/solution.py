def contains_digit(number, digit):

    if str(digit) in str(number):
        return True
    else:
        return False


def main():
    print(contains_digit(123, 4))
    # False
    print(contains_digit(42, 2))
    # True
    print(contains_digit(1000, 0))
    # True
    print(contains_digit(12346789, 5))
    # False

if __name__ == '__main__':
    main()
