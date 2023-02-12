import math

def calculator(num1, operator, num2=None):
    """
    Calculates the result of num1 and num2 based on the operator.
    If the operator is 'sqrt', it returns the square root of num1.
    If the operator is '/' and num2 is 0, it returns "Cannot divide by zero!".
    """
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
        raise ValueError(f"Invalid operator: {operator}")

print("Welcome to Calculator")
first_number = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /,^,sqrt): ")

if operator in ('sqrt','/'):
    result = calculator(first_number, operator)
else:
    second_number = float(input("Enter second number: "))
    result = calculator(first_number, operator, second_number)

print(f"{first_number} {operator} {second_number if operator not in ('sqrt','/') else ''} = {result}")
