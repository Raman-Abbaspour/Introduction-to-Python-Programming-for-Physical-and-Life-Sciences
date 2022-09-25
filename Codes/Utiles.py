"""
Copyright@ 2022 by Raman Abbaspour
All rights reserved. No part of this manual may be reproduced in any manner whatsoever without the written permission
except in case of brief quotations embedded in critical articles or reviews.
"""

# Return sum of a list
def sumList(list):
    sum = 0
    for i in list:
        sum +=i
    return sum

# print elements of a list
def printList(list):
    for i in list:
        print(i)

# Class student
class student:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)







