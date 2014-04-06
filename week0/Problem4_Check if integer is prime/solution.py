def is_prime(n):
    n = abs(n)
    prime = False
    if n == 2:
        prime = True
        return prime

    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                prime
            else:
                prime = True
    return prime


def main():
    print(is_prime(11))
    # True
    print(is_prime(1))
    # False
    print(is_prime(2))
    # True
    print(is_prime(8))
    # False
    print(is_prime(11))
    # True
    print(is_prime(-10))
    # False

if __name__ == '__main__':
    main()
