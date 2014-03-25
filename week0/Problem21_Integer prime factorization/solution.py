def prime_factorization(n):

    count = {}
    x = []
    y = 0
    z = 0
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            x.append(num)

    for j in x:
        if z < j:
            y = 0
            while n != 0 and n % j == 0:
                z = j
                y += 1
                count[j] = y
                n = n // j
    return count


def main():

    print(prime_factorization(10))
    # [(2, 1), (5, 1)] # This is 2^1 * 5^1
    print(prime_factorization(14))
    # [(2, 1), (7, 1)]
    print(prime_factorization(356))
    # [(2, 2), (89, 1)]
    print(prime_factorization(89))
    # [(89, 1)] # 89 is a prime number
    print(prime_factorization(1000))
    # [(2, 3), (5, 3)]

if __name__ == '__main__':
    main()
