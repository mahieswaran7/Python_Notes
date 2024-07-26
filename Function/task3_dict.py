def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def main():
   while True:
        print("\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            print("\nExiting the program...")
            break
        
        if choice.isdigit():
            choice = int(choice)
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue

            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            operations = {
                1: ("Addition", add(num1, num2)),
                2: ("Subtraction", subtract(num1, num2)),
                3: ("Multiplication", multiply(num1, num2)),
                4: ("Division", divide(num1, num2))
            }

            operation_name, result = operations[choice]
            print(f"\n{operation_name} result: {result}")

        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
