"""
Module for performing basic arithmetic operations.

This module provides a function `logic` that performs basic arithmetic
operations based on the operator passed to it as an argument. The supported
operations are addition, subtraction, multiplication, division, and
exponentiation.
"""
import addition
import subtraction
import multiplication
import division
import exponentiation

def logic(first_number, operator, second_number):
    """
    Perform basic arithmetic operations based on the operator.

    Args:
        first_number (float or int): The first number in the calculation.
        operator (str): The operator to perform the calculation with. Must be
        one of "+", "-", "*", "/", or "^".
        second_number (float or int): The second number in the calculation.

    Returns:
        float or int: The result of the calculation.
        None: If the operator is invalid.

    """
    if operator == "+":
        return addition.addition(first_number, second_number)
    elif operator == "-":
        return subtraction.subtraction(first_number, second_number)
    elif operator == "*":
        return multiplication.multiplication(first_number, second_number)
    elif operator == "/":
        return division.division(first_number, second_number)
    elif operator == "^":
        return exponentiation.exponentiation(first_number, second_number)
    else:
        print("Invalid operator")
        return None
    