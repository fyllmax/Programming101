#Imports


#Globals


#Function
def nth_fib_lists(listA, listB, n):
    step = 2
    while step < n + 1:
        following = listA + listB
        listA = listB
        listB = following
        step += 1
    return listA

#Main


def main():
    print(nth_fib_lists([1], [2], 1))
    print(nth_fib_lists([1], [2], 2))
    print(nth_fib_lists([1, 2], [1, 3], 3))
    print(nth_fib_lists([], [1, 2, 3], 4))
    print(nth_fib_lists([], [], 100))

#Program run
if __name__ == "__main__":
    main()
