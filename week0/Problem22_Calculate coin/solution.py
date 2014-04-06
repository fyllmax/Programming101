def calculate_coins(sum):

    coins = [100, 50, 20, 10, 5, 2, 1]

    change = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}
    count = 0
    x = 0
    sum = sum * 100
    for i in coins:
        if i < x:
            count = 0
        while sum > 0 and sum >= i:
            x = i
            sum -= i
            count += 1
            change[i] = count

    return change


def main():

    print(calculate_coins(0.53))
    # {1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}
    print(calculate_coins(8.94))
    # {1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}

if __name__ == '__main__':
    main()
