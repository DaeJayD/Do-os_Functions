def smallest_factor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def prime_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

while True:
    print("Select an option:")
    print("1. Find the smallest factor of a number")
    print("2. Find prime numbers in a range")

    choice = input("Enter your choice (1, 2): ")

    if choice == '1':
        n = int(input("Enter an integer >= 2: "))
        print("The smallest factor of", n, "other than 1 is:", smallest_factor(n))

    elif choice == '2':
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        prime_numbers = prime_numbers_in_range(start, end)
        print(f"Prime numbers in the range [{start}, {end}]: {prime_numbers}")
        break