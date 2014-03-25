def simplify_fraction(fraction):

    numerator = fraction[0]
    denominator = fraction[1]

    smaller = 0
    divisor = 0

    if numerator < denominator:
        smaller = numerator
    else:
        smaller = denominator

    for i in range(2, smaller + 1):

        if numerator % i == 0 and denominator % i == 0:
            divisor = i

    if divisor == 0:
        return (int(numerator), int(denominator))
    else:
        return (int(numerator / divisor), int(denominator / divisor))


def main():
    print(simplify_fraction((3, 9)))
    # (1,3)
    print(simplify_fraction((1, 7)))
    # (1,7)
    print(simplify_fraction((4, 10)))
    # (2,5)
    print(simplify_fraction((63, 462)))
    # (3,22)


if __name__ == '__main__':
    main()
