def prepare_meal(number):

    count = 0
    n = number

    while number % 3 == 0:
            number = number // 3
            count += 1

    if n == 0:
        return " "

    if n % 5 == 0 and n % 3 == 0:

        return 'spam ' * count + 'and eggs'

    elif n % 3 == 0:
        # meal = 'spam ' * count
        return ('spam ' * count).strip()

    elif n % 5 == 0:
        return 'eggs'

    else:
        return ""


def main():
    print(prepare_meal(5))
    # 'eggs'
    print(prepare_meal(15))
    # 'spam and eggs'
    print(prepare_meal(45))
    # 'spam spam and eggs'
    print(prepare_meal(3))
    # "spam"
    print(prepare_meal(27))
    # "spam spam spam"
    print(prepare_meal(7))
    # ""


if __name__ == '__main__':
    main()
