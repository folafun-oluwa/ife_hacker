# def operation():
    
# while True:
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose operation (+, -, *, /): ")


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
            print("Error")
    else:
        print("Wrong operation")
