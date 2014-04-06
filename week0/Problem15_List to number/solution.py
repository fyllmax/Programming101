def list_to_number(digits):
    x = []
    for i in range(len(digits)):
        x.append(str(digits[i]))

        y = ''.join(x)

        z = int(y)

    return z


def main():
    print(list_to_number([1, 2, 3]))
    # 123
    print(list_to_number([9, 9, 9, 9, 9]))
    # 99999
    print(list_to_number([1, 2, 3, 0, 2, 3]))
    # 123023

if __name__ == '__main__':
    main()
