def get_numbers():
    numbers = []

    n = int(input("How many numbers do you want to enter? "))

    for i in range(n):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break

            except ValueError:
                print(f"Invalid input! Please enter a valid number for number {i+1}.")

    return numbers


def calculate_sum(numbers):
    return sum(numbers)


def calculate_difference(numbers):
    diff = numbers[0]
    for num in numbers[1:]:
        diff -= num
    return diff


def calculate_product(numbers):
    prod = 1
    for num in numbers:
        prod *= num
    return prod


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


# Main Program
while True:
    print("\n===== BASIC CALCULATOR =====")
    print("1. Sum")
    print("2. Difference")
    print("3. Product")
    print("4. Average")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        numbers = get_numbers()
        print("Sum =", calculate_sum(numbers))

    elif choice == "2":
        numbers = get_numbers()
        print("Difference =", calculate_difference(numbers))

    elif choice == "3":
        numbers = get_numbers()
        print("Product =", calculate_product(numbers))

    elif choice == "4":
        numbers = get_numbers()
        print("Average =", calculate_average(numbers))

    elif choice == "5":
        print("Exiting calculator...")
        break