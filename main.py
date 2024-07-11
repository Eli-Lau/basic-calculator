# main.py - Calculatorrrr
# A basic calculator that can perform addition, subtraction, multiplication, and division.

import calculator_functions as calc


def main():
    print("Welcome to your Calculator!")
    on = True
    while on:
        operation = input("Enter operation:")

        if calc.isOperationValid(operation) == False:
            print("Invalid Operation")

        else:
            num1 = int(input("Enter 1st number:"))
            num2 = int(input("Enter 2nd number:"))
    
            if operation == '+':
                print(f"{num1} + {num2} = {calc.add(num1, num2)}")
        
            elif operation == '-':
                print(f"{num1} - {num2} = {calc.minus(num1, num2)}")
        
            elif operation == '*':
                print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
        
            elif operation == '/':
                print(f"{num1} / {num2} = {calc.divide(num1, num2)}")
        
            else:
                print("Invalid Operation")

            next_calculation = input("Do you want to do another calculation? (Y/N): ")
            if next_calculation == 'N' or next_calculation == 'n':
                print("Aight, see ya!")
                on = False

            else:
                on = True

if __name__ == "__main__":
    main() 