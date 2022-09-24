# Example 1
myList = [1,2,3,4,5]
sumList(myList)
printList(myList)


# Example 2
import Utiles

myList = [1,2,3,4,5]
Utiles.sumList(myList)
Utiles.printList(myList)


# Example 3
from Utiles import sumList, printList

myList = [1,2,3,4,5]
sumList(myList)
printList(myList)

# Example 4
from Utiles import *

myList = [1,2,3,4,5]
sumList(myList)
printList(myList)

# Example 5
from Utiles import student

myStudent = student("Raman")
myStudent.printName()


# Example 6
import Utiles as u  # Utiles is renamed as u

myList = [1,2,3,4,5]
u.sumList(myList)
u.printList(myList)

#Example 7
from Utiles import sumList as s  # sumList is renamed as s

myList = [1,2,3,4,5]
s(myList)


# Example 8 -- math module
import math

print(math.pi)      # pi
print(math.e)       # e
print(math.inf)     # infinity in Python, can be used in calculus

x = 10
y = 5.5
print(math.sqrt(x))     # square root
print(math.log(x, y))   # log(x, base)
print(math.pow(x, y))   # x**y
print(math.sin(x))      # sin function
print(math.floor(y))    # floor of a number


# Example 9 -- numpy
import numpy as np

array = np.array([[1,2],[3,4]]) # Create a matrix
print(array)    # print matrix

print(np.linalg.inv(array))   # find the matrix's inverse
























