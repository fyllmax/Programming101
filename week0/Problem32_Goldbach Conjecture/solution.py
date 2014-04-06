def isPrime(value):
    prime = True
    for i in range(2, value):
        if(value % i == 0):
            prime = False
            break
    return prime


def goldbach(n):
    plist = []
    plist2 = []
    final_list = []

    for i in range(2, n + 1):

        if isPrime(i):
            plist.append(i)

    for i in plist:
        if i <= n / 2:
            plist2.append(i)

    for i in plist2:
        num = n - i
        if isPrime(num) and num != 1:
            final_list.append((i, num))

    return final_list


def main():
    print(goldbach(4))
    # [(2,2)]
    print(goldbach(6))
    # [(3,3)]
    print(goldbach(8))
    # [(3,5)]
    print(goldbach(10))
    # [(3,7), (5,5)]
    print(goldbach(100))
    # [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53 )]

if __name__ == '__main__':
    main()
