'''
this program creates a simple program that allows the user to use calculate simple expressions 
Author:
Sarah Rivera
'''


# create a function for addition 
def addition(x, y):

    return x + y
#create a function for subtraction
def subtraction(x, y):
    return x - y
#create a function for multiplication
def multiplication(x, y):
    return x * y
#create a function for divison and create an error for division by zeri
def division(x, y):
    if y != 0:
        return x / y
    else:
        print("error: division by zero")
        return None
# create a function for modulus and create an error for modulus by zero
def modulus(x, y):
    if y != 0:
        return x % y
    else:
        print("error: modulus by zero")
        return None
# create function for power
def power(x, y):
    return x ** y
# create a function for floor division and create error for floor division by zero
def floor_division(x, y):
    if y != 0:
        return x // y
    else:
        print("Error: Floor division by zero")
        return None
# create a function anmd loop for the program 'calculator'
def calculator():
    stop = ['quit', 'q']
#create barries for the program- if they meet qualifications allow to type in the expression 
    while True:
        expression = input(":> ")
#command words to break the loop        
        if expression.lower() in stop:
            break
#use the split() funtion in order to create the proper format         
        try:
            x, operator, y = expression.split()
            x = float(x)
            y = float(y)
# elif statements for the operations 
            if operator == '+':
                result = addition(x, y)
            elif operator == '-':
                result = subtraction(x, y)
            elif operator == '*':
                result = multiplication(x, y)
            elif operator == '/':
                result = division(x, y)
            elif operator == '%':
                result = modulus(x, y)
            elif operator == '**':
                result = power(x, y)
            elif operator == '//':
                result = floor_division(x, y)
#create an error for an invalid operator 
            else:
                print(f"error: operator {operator} not allowed  ")
                continue

            print("Result:", result)
# use 'except' to block out invalid expression formats (needs space in b/t operators)
        except ValueError:
            print("error: expression format invalid")
#call the main function to exceute the program 
if __name__ == "__main__":
    calculator()