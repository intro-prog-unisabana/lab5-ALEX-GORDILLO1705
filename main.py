from utils import *

while True:
    operation = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

    if operation == "exit":
        break

    elif operation in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide"]:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = sub(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "exponent":
            result = exponent(num1, num2)
        elif operation == "modulo":
            result = modulo(num1, num2)
        elif operation == "floor_divide":
            result = floor_divide(num1, num2)

        print(f"The result is: {result}")

    elif operation == "absolute":
        num = float(input("Enter the number:\n"))
        result = absolute(num)
        print(f"The result is: {result}")

    else:
        print("Invalid option!")