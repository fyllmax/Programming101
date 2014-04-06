def contains_digit(number, digit):
    x = str(number)

    if str(digit) in x:
        return True
    else:
        return False

def main():
    print (contains_digit(12346789, 5))
    # False
    print (contains_digit(123, 4))
    # False
    print (contains_digit(42, 2))
    # True
    print (contains_digit(1000, 0))
    # True

if __name__ == '__main__':
    main()
