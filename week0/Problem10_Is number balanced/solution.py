def is_number_balanced(n):
    sum1 = 0
    sum2 = 0
    x = str(n)
    y = len(x)
    z = y // 2

    if y % 2 != 0:
        a = x[0: z]
        b = x[z + 1:]

    else:
        a = x[0: z]
        b = x[z:]

    for i in a:
        c = int(i)
        sum1 = sum1 + c

    for j in b:
        d = int(j)
        sum2 = sum2 + d

    if sum1 == sum2:
        return True
    else:
        return False


def main():
    print(is_number_balanced(9))
    # True
    print(is_number_balanced(11))
    # True
    print(is_number_balanced(13))
    # False
    print(is_number_balanced(121))
    # True
    print(is_number_balanced(4518))
    # True
    print(is_number_balanced(28471))
    # False
    print(is_number_balanced(1238033))
    # True
if __name__ == '__main__':
    main()
