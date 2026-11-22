def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Choose an operation (+, -, *, /): ")

    if choice == "+":
        print("Result:", add(num1, num2))
    elif choice == "-":
        print("Result:", subtract(num1, num2))
    elif choice == "*":
        print("Result:", multiply(num1, num2))
    elif choice == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation selected.")

except ValueError:
    print("Error: Please enter valid numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")