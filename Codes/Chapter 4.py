# Example 1
a = "This is a string"
b = 'This is also a string'
c = """When the text spans multiple lines,
We can use triple quotation, like this example.
The output of will also span multiple lines."""
print(c)

# Example 2
a = """First line
Second line
Third line"""
print(a)
print("~~~~~")
b = "First line\nsecond line\nthird line"
print(b)
print("~~~~~")
c = "First line\n second line\n third line"
print(c)

# Table examples
print("He\'s going")
print("The \"book\"")
print("Line one\nLine two")
print("One\tTwo")
print("Using \\ char")

# Example 3
a = "String one"
b = "String two"
plus = "plus"
c = a + plus + b
print(c)

# Example 4
a = "String one "
b = "String two "
plus = "plus "
c = a + plus + b
print(c)

# Example 5
a = "String one"
b = "String two"
plus = "plus"
c = a + " " + plus + " " + b
print(c)

# Example 6
string = "You are "
age = 50
print(string + age)

# Example 7
string = "You are "
age = 50
print(string + str(age))

# Example 8
int("10")       # Valid
float("10")     # Valid
str(10)         # Valid
str(10.0)       # Valid
int(10.5)       # Valid
float(10)       # Valid
int("a")        # Invalid
int("10.5")     # Invalid

# Example 9
name = input("Please type you name: ")
print("Inputted name: " + name)

# Example 10
name = input("Please type you name: ")
lastName = input("Please type you last name: ")
country = input("Please type you country: ")
print("You are " + name + " " + lastName + ". " + "You leave in "
      + country + ".")

# Example 10
atom = "Neon"
protonCount = 10
atomicMass = 20.1797
meltingPoint = -248.60
print(atom + " " + "has " + str(protonCount) + " " +
      "protons with atomic mass of " + str(atomicMass) +
      " " + "u and melting point of " + str(meltingPoint) +
      " C.")

# Example 11
print("%s has %d protons with atomic mass of %f u and melting point of %f C."
      % (atom, protonCount, atomicMass, meltingPoint))

# Example 12
print("%s has %d protons with atomic mass of %.3f u and melting point of %.2f C."
      % (atom, protonCount, atomicMass, meltingPoint))

# Example 13
atom = "Neon"
protonCount = 10
atomicMass = 20.1797
meltingPoint = -248.60
print(f"{atom} has {protonCount} protons with atomic mass of {atomicMass} u and melting point of {meltingPoint} C.")

# Example 14
print(f"{atom} has {protonCount} protons with atomic mass of {atomicMass:.3f} u and melting point of {meltingPoint:.2f} C.")


# BMI Calculator
mass = float(input("Please type your mass in kg: "))
height = float(input("Please type your height in m: "))
BMI = mass / (height**2)    # BMI in kg/m^2
print(f"With the mass of {mass:.2f} kg and height of {height:.2f} m, your BMI is {BMI:.2f}")

# Example 15
text = "Computer Science"
firstChar = text[0]
secondChar = text[1]
print(f"First Char: {firstChar}")
print(f"Second Char: {secondChar}")

# Example 16
text = "Computer Science"
lastChar = text[-1]
secondLastChar = text[-2]
print(f"Last Char: {lastChar}")
print(f"Second Last Char: {secondLastChar}")

# Example 17
text = "Computer Science"
print(f"Length of text is {len(text)}.")

# Example 18
text = "Computer Science"
lastChar = text[len(text)-1]
print(f"The last character is {lastChar}.")

# Example 19
text = "Computer Science"
a = text[24]
b = text[16]
c = text[-50]

# Example 19
text = "Computer Science"
seq = text[5:10]
print(f"The fifth to ninth element are: {seq}")

# Example 19
text = "Computer Science"
print(f"No start index: {text[:10]}")
print(f"No end index: {text[10:]}")
print(f"No start/end index: {text[:]}")

# Example 20: upper, lower, capitalize, title methods
text = "Computer Science is fun."
upperText = text.upper()         # All characters to upper case
lowerText = text.lower()         # All characters to lower case
capText = text.capitalize()      # Only the first character to upper case
titleText = text.title()         # First character of every word to upper case
print(f"""
Original: {text}
Upper: {upperText} 
Lower: {lowerText}
Capitalize: {capText}
Title: {titleText}""")

# Example 21: find methods
text = "Computer Science is fun."
findScience = text.find("Science")      # Finds the start index of a phrase
findPatience = text.find("patience")
findE = text.find("e", 8)              # Finds the phrase starting from the given index
replacesText = text.replace("Science", "programming") # Replaces a phrase with a new one
print(f"""
Science index: {findScience}
patience: {findPatience} 
e index: {findE}
repace: {replacesText}""")

# Example 22: replace, strip method
text = "         Computer Science is fun.   "
replaceSpace = text.replace(" ", "_")   # Replaces a phrase with a new one
replacesScience = text.replace("Science", "programming")
stripedText = text.strip()      # Removes spaces before and after the string
print(f"""
Original text: {text}
Replaced Science: {replacesScience}
Replaced Spaces: {replaceSpace}
Stripped text: {stripedText}""")


# Example 23: isupper, islower, isdigit methods
text = "computer science is fun."
isUpper = text.isupper()     # True if all characters are upper case
isLower = text.islower()     # True if all characters are lower case
isDigit = text.isdigit()     # True if all characters are digits
print(f"""
Are all characters upper: {isUpper}
Are all characters lower: {isLower} 
Are all characters digits: {isDigit}""")

# Example 24: combination of methods
text = "          computer science is fun and Interesting.     "
finalText = text.strip().title().replace(" ", "_" )[:23]
print(f"""
Original text: {text}
Final text: {finalText}""")