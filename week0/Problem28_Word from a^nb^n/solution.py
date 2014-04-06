def is_an_bn(word):
    an_bn = False

    if len(word) == 0:
        an_bn = True
        return an_bn

    x = len(word) // 2
    lst1 = list(word[: x])
    lst2 = list(word[x:])

    if lst1[0] == 'a' and lst2[0] == 'b':

        for i in lst1:
            if 'b' not in lst1:
                an_bn = True
            else:
                return an_bn

        for i in lst2:
            if 'a' not in lst2:
                an_bn = True
            else:
                return an_bn
    return an_bn


def main():
    print(is_an_bn(""))
    # True
    print(is_an_bn("rado"))
    # False
    print(is_an_bn("aaabb"))
    # False
    print(is_an_bn("aaabbb"))
    # True
    print(is_an_bn("aabbaabb"))
    # False
    print(is_an_bn("bbbaaa"))
    # False
    print(is_an_bn("aaaaabbbbb"))
    # True


if __name__ == '__main__':
    main()
