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