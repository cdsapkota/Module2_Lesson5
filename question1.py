def add(a, b):
    sum = a + b
    return sum
    
def subtract(a, b):
    sub = a - b
    return sub

def multiply(a, b):
    mult = a * b
    return mult

def division(a, b):
    try:
        div = round( (a / b), 2)
    except ZeroDivisionError:
        return "Error: Division by zero is frowned upon."
    return div

def calculation():
    operation = input("What would you like to do (addition, subtraction, multiplication or division)? ")
    
    if operation.lower() in ["addition", "subtraction", "multiplication", "division"]:
        try:
            number_1 = int(input("What is your first number? "))
            number_2 = int(input("What is your second number? "))
        except ValueError:
            print("Error: Please enter valid number.")
            return

        if operation.lower() == "addition":
            result = add(number_1, number_2)
        elif operation.lower() == "subtraction":
            result = subtract(number_1, number_2)
        elif operation.lower() == "multiplication":
            result = multiply(number_1, number_2)
        elif operation.lower() == "division":
            result = division(number_1, number_2)
        print(f"The {operation} of {number_1} and {number_2} is {result}.")
    else:
        print("Incorrect request.")
            

calculation()