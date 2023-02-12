"""
This module performs basic arithmetic operations based on user input.

The module imports `input_module` and `logic` to retrieve two numbers and an
operator from the user and calculate the result of the operation. The result of
the calculation is printed if it is not None.
"""
if __name__ == "__main__":
    import input_module
    import logic

    first_number = input_module.get_number()
    operator = input_module.get_operation()
    second_number = input_module.get_number()

    result = logic.logic(first_number, operator, second_number)
    if result is not None:
        print(f"Result: {result}")
