history = []

def show_menu():
    print("\n===== Smart Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")

def calculate(choice, a, b):
    if choice == "1":
        return a + b
    elif choice == "2":
        return a - b
    elif choice == "3":
        return a * b
    elif choice == "4":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

operations = {"1": "+", "2": "-", "3": "*", "4": "/"}

while True:
    show_menu()
    choice = input("Enter choice (1-6): ")

    if choice == "6":
        print("Goodbye 👋")
        break

    elif choice == "5":
        print("\n--- Calculation History ---")
        if not history:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    elif choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculate(choice, a, b)

            output = f"{a} {operations[choice]} {b} = {result}"
            print("Result:", result)

            history.append(output)

        except ValueError:
            print("Invalid input! Please enter numbers.")

    else:
        print("Invalid choice. Try again.")
