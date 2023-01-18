import operator

# Define a dictionary of operations
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculator(num1, operator, num2):
    try:
        return operations[operator](num1, num2)
    except KeyError:
        return "Invalid operator"
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print("Welcome to Calculator.py")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = calculator(num1, operator, num2)
print(num1, operator, num2, "=", result)
