def sum_of_min_and_max(arr):

    if len(arr) > 0:
        return max(arr) + min(arr)

    else:
        return "array is emtpy"


def main():
    print(sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]))
    # 10
    print(sum_of_min_and_max([-10, 5, 10, 100]))
    # 90
    print(sum_of_min_and_max([1]))
    # 2

if __name__ == '__main__':
    main()
