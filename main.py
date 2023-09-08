import math

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Second number is 0!"

def extract_sqrt(a):
    if a > 0:
        return math.sqrt(a)
    else:
        return "Number is negative!"

def degree(a, b):
    # b - degree
    # a - number
    return a ** b

def inp():
    a = float(input("Input first number: "))
    b = float(input("Input second number: "))
    return a, b

def inp2():
    a = float(input("Input number: "))
    return a

# main
t = True
while t:
    num = int(input("Your choice! \n 1 - Add \n 2 - Subtract \n 3 - Divide \n 4 - Multiply \n 5 - Sqrt extraction \n 6 - Increase degree\n Input number: "))
    
    if num == 1:
        a, b = inp()
        print("Result Add: ", add(a, b))
    elif num == 2:
        a, b = inp()
        print("Result Subtract: ", subtract(a, b))
    elif num == 3:
        a, b = inp()
        print("Result Divide: ", divide(a, b))
    elif num == 4:
        a, b = inp()
        print("Result Multiply: ", multiply(a, b))
    elif num == 5:
        a = inp2()
        print("Result Sqrt: ", extract_sqrt(a))
    elif num == 6:
        a = inp2()
        b = int(input("Input degree: "))
        print("Result Inc. Degree: ", degree(a, b))
    else:
        print("Invalid argument!")
        exit(-1)
    
    con = input("Would you like to continue? \n Input Y (yes) or N (no): ")
    if con.lower() == 'y':
        t = True
    elif con.lower() == 'n':
        t = False
        break
    else:
        print("Invalid argument!")
        exit(-1)