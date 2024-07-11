# calculator functions

def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
        return x / y
    return "Error! No Division by Zero!!"

def isOperationValid(x):
    if x == '+' or x == '-' or x == '*' or x == '/':
        return True
    else:
        return False