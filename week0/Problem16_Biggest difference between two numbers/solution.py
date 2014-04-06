def biggest_difference(arr):

    a = min(arr)
    b = max(arr)

    if a-b > b-a:
        return b-a
    else:
        return a-b

def main():

    print(biggest_difference([1,2]))
    # -1
    print(biggest_difference([1,2,3,4,5]))
    # -4
    print(biggest_difference([-10, -9, -1]))
    # -9
    print(biggest_difference(range(100)))
    # -99

if __name__ == '__main__':
    main()

