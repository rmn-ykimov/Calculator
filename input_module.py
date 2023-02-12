"""
This module provides functions for performing basic arithmetic operations.

The following functions are available:
    - get_number: prompts the user to enter a number and returns it as a float
    - get_operation: prompts the user to enter a valid arithmetic operator and
    returns it as a string
"""

def get_number():
    """
    Get a number from the user.

    This function prompts the user to enter a number and returns the number as
    a float.

    Returns:
        float: A number entered by the user.
    """
    user_input = input("Enter a number: ")
    return float(user_input)

def get_operation():
    """
    Get a valid arithmetic operator from the user.

    This function repeatedly prompts the user to enter an arithmetic operator
    until a valid operator is entered. The valid operators are '+', '-', '*',
    '/', and '^'. The entered operator is returned once it is valid.

    Returns:
        str: A valid arithmetic operator.
    """
    while True:
        user_input = input("Enter an operation (+, -, *, /, ^): ")
        if user_input in ['+', '-', '*', '/', '^']:
            return user_input
        print("Invalid operator. Please enter a valid operator (+, -, *, /, ^).")
