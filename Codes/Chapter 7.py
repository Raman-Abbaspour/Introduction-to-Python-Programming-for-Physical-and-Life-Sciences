"""
Copyright@ 2022 by Raman Abbaspour
All rights reserved. No part of this manual may be reproduced in any manner whatsoever without the written permission
except in case of brief quotations embedded in critical articles or reviews.
"""

# Example 1

number1 = input("Please type the first whole number to be tested: ")
number2 = input("Please type the second whole number to be tested: ")
number3 = input("Please type the third whole number to be tested: ")
number4 = input("Please type the fourth whole number to be tested: ")

if number1.isdigit():
    lastDigit = int(number1[-1])
    if lastDigit == 0:
        print("The last digit of first number is 0")
    elif lastDigit == 1:
        print("The last digit of first number is 1")
    elif lastDigit == 2:
        print("The last digit of first number is 2")
    else:
        print("The last digit of first number is not 0, 1, or 2")
else:
    print("The first number is not a whole number")

if number2.isdigit():
    lastDigit = int(number2[-1])
    if lastDigit == 0:
        print("The last digit of second number is 0")
    elif lastDigit == 1:
        print("The last digit of second number is 1")
    elif lastDigit == 2:
        print("The last digit of second number is 2")
    else:
        print("The last digit of second number is not 0, 1, or 2")
else:
    print("The second number is not a whole number")


if number3.isdigit():
    lastDigit = int(number3[-1])
    if lastDigit == 0:
        print("The last digit of third number is 0")
    elif lastDigit == 1:
        print("The last digit of third number is 1")
    elif lastDigit == 2:
        print("The last digit of third number is 2")
    else:
        print("The last digit of third number is not 0, 1, or 2")
else:
    print("The third number is not a whole number")


if number4.isdigit():
    lastDigit = int(number4[-1])
    if lastDigit == 0:
        print("The last digit of fourth number is 0")
    elif lastDigit == 1:
        print("The last digit of fourth number is 1")
    elif lastDigit == 2:
        print("The last digit of fourth number is 2")
    else:
        print("The last digit of fourth number is not 0, 1, or 2")
else:
    print("The fourth number is not a whole number")

print("Ends of program")

# Example 2
def myFunction(number, countString):
    if number.isdigit():
        lastDigit = int(number[-1])
        if lastDigit == 0:
            print(f"The last digit of {countString} number is 0")
        elif lastDigit == 1:
            print(f"The last digit of {countString} number is 1")
        elif lastDigit == 2:
            print(f"The last digit of {countString} number is 2")
        else:
            print(f"The last digit of {countString} number is not 0, 1, or 2")
    else:
        print(f"The {countString} number is not a whole number")

number1 = input("Please type the first whole number to be tested: ")
number2 = input("Please type the second whole number to be tested: ")
number3 = input("Please type the third whole number to be tested: ")
number4 = input("Please type the fourth whole number to be tested: ")

myFunction(number1, "first")
myFunction(number2, "second")
myFunction(number3, "third")
myFunction(number4, "fourth")

print("Ends of program")

# Example 3
def BMI(mass, height):
    bmi = mass / height**2
    return bmi


# Example 4 -- calling BMI by positional argument
massInput = float(input("Please type in your mass in kg: "))
heightInput= float(input("Please type in your height in m: "))
bmi = BMI(massInput, heightInput)   # Arguments must be in order
print(bmi)

# Example 5 -- calling BMI by keyword arguments
massInput = float(input("Please type in your mass in kg: "))
heightInput= float(input("Please type in your height in m: "))
# Assign each parameter to each argument, order is not needed.
bmi = BMI(height=heightInput, mass= massInput )
print(bmi)

# Example 6 -- calling BMI by positional and keyword argument
massInput = float(input("Please type in your mass in kg: "))
heightInput= float(input("Please type in your height in m: "))
# Arguments must be in order. Positional argument must come before keyword arguments
bmi = BMI(massInput, height=heightInput)
print(bmi)


# Example 7 -- optional arguments
def BMI(mass, height, printBMI = False):
    bmi = mass / height**2
    if printBMI:
        print(f"{bmi:.2f}")
    return bmi

massInput = float(input("Please type in your mass in kg: "))
heightInput= float(input("Please type in your height in m: "))
bmi = BMI(massInput, height=heightInput)    # printBMI is optional and excluded
print(bmi)

massInput = float(input("Please type in your mass in kg: "))
heightInput= float(input("Please type in your height in m: "))
bmi = BMI(massInput, heightInput, printBMI=True)
print(bmi)

# Example 8
def changeNumber(number):
    number = 20

number = 10
changeNumber(number)
print(number)


# Example 9
def someFunction():
    b = 10
    c = 12
    print(f"Function: {a}")
    print(f"Function: {b}")
    print(f"Function: {c}")

a = 25
someFunction()
print(f"Outside Function: {a}")
print(f"Outside Function: {b}")
print(f"Outside Function: {c}")

# Example 10 -- global variable
def someFunction():
    global b        # This variable is now global, not local
    global c
    b = 10
    c = 12
    print(f"Function: {a}")
    print(f"Function: {b}")
    print(f"Function: {c}")

a = 25
someFunction()
print(f"Outside Function: {a}")
print(f"Outside Function: {b}")
print(f"Outside Function: {c}")



# Example 11
def changeNumber(number):
    number[0] = 20

number = [10]
changeNumber(number)
print(number)

# Example 12
def myFunction(theList, theNumber):
    finalAnswer = theNumber*multiplier
    theList[1] = finalAnswer
    return finalAnswer


number = 3
multiplier = 2
myList = [2,1,5]
answer = myFunction(myList, number)
print(answer)
print(myList)

