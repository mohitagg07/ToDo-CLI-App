# calculator.py

# Functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero"
    return a / b

# Function to get user's choice
def get_choice():
    print("\n🔢 Calculator Menu:")
    print("1 ➤ Add")
    print("2 ➤ Subtract")
    print("3 ➤ Multiply")
    print("4 ➤ Divide")
    print("5 ➤ Exit")

    return input("Choose an option (1–5): ")

# Function to get user input numbers
def get_numbers():
    try:
        num1 = float(input("Enter first number ➜ "))
        num2 = float(input("Enter second number ➜ "))
        return num1, num2
    except ValueError:
        print("❌ Please enter valid numbers.")
        return None, None

# Main loop using conditionals and functions
def calculator():
    while True:
        choice = get_choice()

        if choice == "5":
            print("👋 Exiting Calculator. Thank you!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue

            if choice == "1":
                result = add(num1, num2)
                print(f"✅ Result: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"✅ Result: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"✅ Result: {num1} × {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            print("⚠️ Invalid option. Please choose from 1 to 5.")

# CLI entry point
if __name__ == "__main__":
    calculator()
