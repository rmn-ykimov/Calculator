import operator
import math

def calculator(num1, operator, num2):
    try:
        if operator == '+':
            return operator.add(num1, num2)
        elif operator == '-':
            return operator.sub(num1, num2)
        elif operator == '*':
            return operator.mul(num1, num2)
        elif operator == '/':
            return operator.truediv(num1, num2)
        elif operator == '^':
            return operator.pow(num1, num2)
        elif operator == 'sqrt':
            return math.sqrt(num1)
        else:
            raise ValueError("Invalid operator")
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print("Welcome to Calculator.py")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /,^,sqrt): ")
if operator != 'sqrt':
    num2 = float(input("Enter second number: "))
    result = calculator(num1, operator, num2)
else:
    result = calculator(num1, operator, None)

print(num1, operator, num2 if operator != 'sqrt' else '', "=", result)
