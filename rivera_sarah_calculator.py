""" 
Simple Calculator 
Author: Sarah Rivera 
"""


def simple_calculator(expression_str):
    # Split the expression into parts
    expression = expression_str.split()

    # Extract the operator and numbers
    num1 = float(expression[0])
    op = expression[1]
    num2 = float(expression[2])

    # Check for division operation
    if op == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero."
        else:
            result = num1 / num2
            return f"The quotient is {result}."
    elif op == '+':
        result = num1 + num2
        return f"The sum is {result}."
    elif op == '-':
        result = num1 - num2
        return f"The difference is {result}."
    elif op == '*':
        result = num1 * num2
        return f"The product is {result}."
    else:
        # Handle invalid operator
        return "Error: Invalid operator entered."

