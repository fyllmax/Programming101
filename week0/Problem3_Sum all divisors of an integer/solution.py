def sum_of_divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum = sum + i
    return sum


def main():
    print(sum_of_divisors(8))
    # 15
    print(sum_of_divisors(7))
    # 8
    print(sum_of_divisors(1))
    # 1
    print(sum_of_divisors(1000))
    # 2340

if __name__ == '__main__':
    main()
