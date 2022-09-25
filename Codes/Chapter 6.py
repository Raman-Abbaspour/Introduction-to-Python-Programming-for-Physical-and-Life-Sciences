"""
Copyright@ 2022 by Raman Abbaspour
All rights reserved. No part of this manual may be reproduced in any manner whatsoever without the written permission
except in case of brief quotations embedded in critical articles or reviews.
"""

# Example 1
myList = [1,2,3,4,5]
print(myList)

# Example 2
myList = [1,"hello", 6.5,5]
print(myList)


# Example 3
myList = [1,2,[3,4], [5,6]]
print(myList)


# Example 4
myList = [1,2,3,4,5,6,7,8,9]
length = len(myList)
third_Element = myList[3]
second_To_Last_Element = myList[-1]
third_To_Fifth_Element = myList[3:6]    # including the fifth element
fourth_To_Last_Element = myList[4:]
start_To_Fourth_Element = myList[:4]
allElements = myList[:]
print(f"""
Third Element: {third_Element}
second to Last Element: {second_To_Last_Element}
Third To Fifth Element: {third_To_Fifth_Element}
Fourth To Last Element: {fourth_To_Last_Element}
Start To Fourth Element: {start_To_Fourth_Element}
All Elements: {allElements}
Length: {length}
""")

# Example 5
myList = [1,2,3,4,5,6,7,8,9]
myList[3] = "hello world"
print(myList)





# Example 6 -- append
myList = [1,1,2,2,2,5,6,7]
myList.append(12)
print(myList)


# Example 7 -- insert
myList = [1,1,2,2,2,5,6,7]
# ass 12 to index 3, all elements from index 4 will be shift to the right
myList.insert(3,12)
print(myList)



# Example 8 -- remove
myList = [1,1,2,2,2,5,6,7]
myList.remove(2)    # Only the first instance will be removed
print(myList)


# Example 9 -- index, count
myList = [1,1,2,2,2,5,6,7]
two_index = myList.index(2)     # Only the index of the first instance will be returned
two_count = myList.count(2)
print(f""""
Index of first 2: {two_index}
Number of 2 in the list: {two_count}""")


# Example 10 -- count, index
myList = [1,1,2,2,2,5,6,7]
myList.append(12)
print(myList)


# Example 11 -- copy, clear
myList = [1,1,2,2,2,5,6,7]
newList = myList.copy()
# The original list will be cleared, but the copy will not be affected.
myList.clear()
print(f"""
myList: {myList}
new List: {newList}
""")


# Example 12 -- reverse
myList = [1,1,2,2,2,5,6,7]
myList.reverse()
print(myList)


# Example 13 -- sort
myList = [5,2,8,6,78,2,5,1,1]
myList.sort()
print(myList)


# Example 14
myList = [5,2,8,6,78]
for i in myList:
    print(i)

# Example 15
for i in range(len(myList)):
    print(myList[i])

# Example 16
mySet = {2,2,5,9}   # Python automatically removes one of the 2s
print(mySet)

# Example 17
myTuple = (3,5,5)
print(myTuple)

# Example 18
myTuple = (3,5,5)
a, b, c = myTuple
print(f"""
Tuple: {myTuple}
a: {a}
b: {b}
c: {c}
""")

# Example 19
myDict = {"City": "Toronto", "Country":"Canada"} # Key:Value
print(myDict)


# Example 20
myDict = {"City": "Toronto", "Country":"Canada"}
print(f"""
City: {myDict["City"]}          
Country: {myDict["Country"]}
""")


# Example 21
myDict = {"City": "Toronto", "Country":"Canada", "Age": 25}
print(f"""
mydict: {myDict}          
Keys: {list(myDict.keys())}
Values: {list(myDict.values())}
Items: {list(myDict.items())}
""")


# Example 22
myDict = {"City": "Toronto", "Country":"Canada", "Age": 25}
for keys in myDict.keys():
    print(f"Key: {keys}, Value: {myDict[keys]}")


# Example 23
myDict = {"City": "Toronto", "Country":"Canada", "Age": 25}
for keys, values in myDict.items():
    print(f"Key: {keys}, Value: {values}")

# Example 24
myList = [1,2,4, "hello", [1,2]]
if 2 in myList:
    print("2 exists in the list")
else:
    print("2 does not exists in the list")

# Example 25
myDict = {"City": "Toronto", "Country":"Canada", "Age": 25}
if "City" in myDict.keys():
    print("City key exists")
else:
    print("City key does not exists")



