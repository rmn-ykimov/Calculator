import math

def calculator(num1, operator, num2=None):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2
    elif operator == '^':
        return num1 ** num2
    elif operator == 'sqrt':
        return math.sqrt(num1)
    else:
        raise ValueError("Invalid operator")

print("Welcome to Calculator.py")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /,^,sqrt): ")
if operator != 'sqrt':
    num2 = float(input("Enter second number: "))
    result = calculator(num1, operator, num2)
else:
    result = calculator(num1, operator)

print(num1, operator, num2 if operator != 'sqrt' else '', "=", result)
