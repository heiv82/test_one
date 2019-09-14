import math

choise = 0
def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def dividing(a, b):
    return a / b

def input_number():
    global a, b
    a = int(input("Please input first number: "))
    b = int(input("Please input second number: "))
    return a,b

while(True):
    print("Welcome to calculate!")
    print("Please to choose what do you want to do: ")
    print("Press 1 === addition")
    print("Press 2 === substraction")
    print("Press 3 === multiplication")
    print("Press 4 === dividing")
    print("Press 5 === involution:")
    print("Press 6 === dividing without .... : ")
    print("Press 0 === finish")
    print()
    choise = int(input())

    if choise == 1:
        input_number()
        print("It is - ", addition(a,b),"\n")
    elif choise == 2:
        input_number()
        print("\nThe answer is ", substraction(a, b),"\n")
    elif choise == 3:
        input_number()
        print("\nThe answer is ", multiplication(a,b),"\n")
    elif choise == 4:
        input_number()
        print("\nThe answer is ", dividing(a, b),"\n")
    elif choise == 5:
        a = int(input("Enter a number: "))
        b = int(input("Enter an exponent: "))
        print("\nThe answer is ", a**b, "\n")
    elif choise == 6:
        input_number()
        print("\nThe answer is ", a // b, "\n")
    elif choise == 0:
        print("""
        ====================
        ====================
              Buy buy
        ====================
        ====================
        """)
        break






