# Imports


# Globals


# Function
def nth_fibonacci(n):
    if n < 2:
        return n
    return nth_fibonacci(n - 2) + nth_fibonacci(n - 1)


# Main
def main():
    print(nth_fibonacci(2))
    print(nth_fibonacci(3))
    print(nth_fibonacci(10))


# Program run
if __name__ == "__main__":
    main()
