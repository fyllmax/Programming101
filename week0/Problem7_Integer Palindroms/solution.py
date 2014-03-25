def is_int_palindrom(n):

    x = str(n)
    y = ''
    for i in x[::-1]:
        y = str(y + i)

    if y == x:
        return True
    else:
        return False


def main():
    print (is_int_palindrom(1))
    # True
    print (is_int_palindrom(42))
    # False
    print (is_int_palindrom(100001))
    # True
    print (is_int_palindrom(999))
    # True
    print (is_int_palindrom(123))
    # False

if __name__ == '__main__':
    main()
