def calNum(operation, num1, num2):
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    operation = input("Choose operation (+, -, *, /): ")

    while operation not in ["+", "-", "*", "/"]:
        print("Invalid operation. Please choose one of +, -, *, /.")
        operation = input("Choose operation (+, -, *, /): ")

    calNum(operation, num1, num2)

main()