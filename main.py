import math

def calculator(num1, operator, num2=None):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero!"
    elif operator == '^':
        return num1 ** num2
    elif operator == 'sqrt':
        return math.sqrt(num1)
    else:
        raise ValueError("Invalid operator")

print("Welcome to Calculator.py")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /,^,sqrt): ")

result = calculator(num1, operator, float(input("Enter second number: ")) if operator not in ('sqrt','/') else None)
print(num1, operator, num2 if operator not in ('sqrt','/') else '', "=", result)
