"""
Copyright@ 2022 by Raman Abbaspour
All rights reserved. No part of this manual may be reproduced in any manner whatsoever without the written permission
except in case of brief quotations embedded in critical articles or reviews.
"""

# Example 1
a = True
b = False
print(f"a is {a} while b is {b}")

# Example 2
a = 10
b = 5
print(f"a==b : {a==b}")
print(f"a>b  : {a>b}")
print(f"a<b  : {a<b}")
print(f"a>=b : {a>=b}")
print(f"a<=b : {a<=b}")
print(f"a!=b : {a!=b}")

# Example 2
input1 = float(input("Please type the first number: "))
input2 = float(input("Please type the second number: "))
input3 = float(input("Please type the third number: "))
oneEqualTwo = input1 == input2
threeEqualOne = input1 == input3
allEqual = oneEqualTwo == threeEqualOne
print(f"The result is {allEqual}")

# Example 3
input1 = float(input("Please type the first number: "))
input2 = float(input("Please type the second number: "))
input3 = float(input("Please type the third number: "))
allEqual = ((input1 == input2) and (input1 == input3))
print(f"The result is {allEqual}")

# Example 4
number = input("Please type a whole number: ")
if number.isdigit():
    print(f"The input was {number}")

print(f"Ends of program")

# Example 5
number = input("Please type a whole number: ")

if number.isdigit():
    print("The input was {number}")
if not number.isdigit():
    print("Not a whole number")

print("Ends of program")

# Example 6
number = input("Please type a whole number: ")

if number.isdigit():
    print(f"The input was {number}")
else:
    print("Not a whole number")

print("Ends of program")


# Example 7
number = input("Please type a whole number to be tested: ")

if number.isdigit():
    lastDigit = int(number[-1])
    if lastDigit == 0:
        print("The last digit is 0")
    elif lastDigit == 1:
        print("The last digit is 1")
    elif lastDigit == 2:
        print("The last digit is 2")
    else:
        print("The last digit is not 0, 1, or 2")
else:
    print("Not a whole number")

print("Ends of program")


# Example 8
number = input("Please type a whole number to be tested: ")

if number.isdigit():
    lastDigit = int(number[-1])
    if lastDigit == 0:
        print("The last digit is 0")
    elif lastDigit == 1:
        # Because of pass, if the last digit is 1, nothing will be printed
        pass
        print("The last digit is 1")
    elif lastDigit == 2:
        print("The last digit is 2")
    else:
        print("The last digit is not 0, 1, or 2")
else:
    print("Not a whole number")

print("Ends of program")


# Example 9
number = input("Please type a whole number: ")

while not number.isdigit():
    number = input("Please type a whole number: ")

print(f"The input was {number}")


# Example 10
counter = 0
while counter<6:
    print(f"Counter at {counter}")
    counter += 1 # counter = counter + 1

print("End of program")

# Example 11
for counter in range(6):
    print(f"Counter at {counter}")

print("End of program")

# Example 12
for i in range(10,19):
    if i % 2 != 0:
        continue
    print(f"{i // 2}th even number is {i}")

print("End of program")


# Example 13
for i in range(10000):
    if i == 3:
        break
    print(f"Iteration {i}")

print("End of program")


# Example 14 --- DO NOT RUN THIS
for i in range(10000):
    for j in range(10000):
        for k in range(10000):
            print(f"Hello World")



# Exercise 6
i = 22
while (i > 12):
    for j in range (100, -50, -20):
        print(f"{j} Hello World")
    i -=3













































































