print("=== Simple Calculator ===")

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("\nError! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")

        else:
            print("\nInvalid choice! Please select 1, 2, 3, or 4.")

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the calculator!")
            break

    except ValueError:
        print("\nInvalid input! Please enter numeric values only.")