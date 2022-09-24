# Example 1

def concat(stringList):
    answer = ""
    for i in stringList:
        answer += i
        answer += " "
    return answer



newString  = concat(["Hello", "world.", "This", "is", "Raman."])
print(newString)


newString  = concat(12)

# Example 2
def concat(stringList):
    # This asserts if the list is empty or not
    assert len(stringList) > 0, "The list is empty"
    answer = ""
    for i in stringList:
        # This asserts if the list only contains string
        assert type(i) == str, "At least one element is not string"
        answer += i
        answer += " "
    return answer

newString  = concat([])
newString  = concat(["hello", 2])

# try-except syntax
# try:
#     statement
#     ...
# except:
#     statement
#     ...

# Example 3
try:
    newString = concat([])
    print("try-statement is done")
except:
    print("an error has occurred")

# Example 4
try:
    newString = concat(["hello", " world"])
    print("try-statement is done")
except:
    print("an error has occurred")

# try-except syntax
# try:
#     statement
#     ...
# except ErrorType:
#     statement
#     ...
# except AnotherErrorType:
#     statement
#     ...
# except YetAnotherErrorType:
#     statement
#     ...
# except:
#     statement
#     ...

# Example 5
try:
    newString = concat([])
except AssertionError:
    print("AssertionError has occurred")
except TypeError:
    print("TypeError has occurred")
except:
    print("Another error has occured")

# Example 6
try:
    newString = concat()
except AssertionError:
    print("AssertionError has occurred")
except TypeError:
    print("TypeError has occurred")
except:
    print("Another error has occured")

# Example 7
try:
    newString = aa
except AssertionError:
    print("AssertionError has occurred")
except TypeError:
    print("TypeError has occurred")
except:
    print("Another error has occured")


# Example 8
while True:
    try:
        number = int(input("Please input a digit: "))
        break
    except:
        pass

print("End of Program")


# Example 8
number = int(input("Please input a digit: "))
if number ==2:
    raise Exception

print("End of Program")


# Debugging


# Example
def retrunSecondElement(list):
    element = list[2]
    return element

myList = [0,1,2,3,4,5]
output = retrunSecondElement(myList)
print(output)























































