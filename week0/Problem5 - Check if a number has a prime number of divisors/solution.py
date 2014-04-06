# Imports


# Globals


# Function
def prime_number_of_divisors(n):
    count = 0
    prime = False

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        prime = True
        return prime

    if count > 2:
        for j in range(2, count + 1):
            if count % j == 0:
                break
            else:
                prime = True
    return prime


# Main


def main():
    print(prime_number_of_divisors(7))
    # True
    print(prime_number_of_divisors(8))
    # False
    print(prime_number_of_divisors(9))
    # True

# Program run
if __name__ == "__main__":
    main()
