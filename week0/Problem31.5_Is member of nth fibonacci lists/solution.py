# Imports


# Globals


# Function
def member_of_nth_fib_lists(listA, listB, needle):
    step = 2
    while step < len(needle) + 1:
        following = listA + listB
        listA = listB
        listB = following
        step += 1

        if listB == needle:
            return True

    return False


# Main
def main():
    print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
    # False
    print(member_of_nth_fib_lists([1, 2],
          [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
    # True
    print(member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
    # True
    print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))
    # False


# Program run
if __name__ == "__main__":
    main()
