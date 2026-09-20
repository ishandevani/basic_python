def add(a, b):
    return a + b

def subtr(a, b):
    return a -b

def multi(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return a/b

while True:
    print("Select an Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ").strip()

    if choice == '5':
        print("Exit code")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
                print("Invalid Value!, Please enter a valide number.")
                continue

        try:
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtr(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multi(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divi(num1, num2)}")

        except ZeroDivisionError as e:
                print(e)
    else:
        print("Invalid Choice! Please select a valid option from the menu.")