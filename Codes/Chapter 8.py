# Example 1 -- School and students

def addStudentToSchool(schoolList, studentName):
    """Adds student to school student list"""
    schoolList.append(studentName)

def printSchoolStudents(SchoolList):
    """Prints the name of students in a given school"""
    print(SchoolList)

def printStudentAge(name, studentNameList,studentAgeList):
    """Prints the age of student"""
    for i in range(len(studentNameList)-1):     # Find the index of student's age
        if studentNameList[i] == name:
            break
    print(studentAgeList[i])

school1 = "Elementary"
school1_location = "Toronto"
school1_total_student = 300
school1_student_list = []

school2 = "Secondary"
school2_location = "Toronto"
school2_total_student = 500
school2_student_list = []

# Student Definition
def printStudentName(name):
    """Prints the name of student"""
    print(name)

def printStudentLastName(lastName):
    """Prints the name of student"""
    print(lastName)

student1_name = "Max"
student1_lastName = "Smith"
student1_age = 8

student2_name = "Bob"
student2_lastName = "Patel"
student2_age = 10

student3_name = "Alice"
student3_lastName = "Kim"
student3_age = 16

student4_name = "Sara"
student4_lastName = "William"
student4_age = 17

student5_name = "Ross"
student5_lastName = "Long"
student5_age = 16

studentNameList = ["Max", "Bob", "Alice", "Sara", "Ross"]
studentLastNameList = ["Smith", "Patel", "Kim", "William", "Long"]
studentAgeList = [8, 10, 16, 17, 16]

# add the first two students
addStudentToSchool(school1_student_list, "Max")
addStudentToSchool(school1_student_list, "Bob")

# add the next three students
addStudentToSchool(school2_student_list, "Alice")
addStudentToSchool(school2_student_list, "Sara")
addStudentToSchool(school2_student_list, "Ross")

#print the age of "Sara"
printStudentAge("Sara",studentNameList,studentAgeList)

# Example 1 -- School and students -- The correct way, suing OOP
class School:
    def __init__(self, name, location, totalStudent):
        self.name = name
        self.location = location
        self.totalStudent = totalStudent
        self.studentList = []

    def addStudentToSchool(self, *student):
        for i in student:
            self.studentList.append(i)

    def printSchoolStudents(self):
        """Prints the name of students in a given school"""
        for i in self.studentList:
            print(i.name)

    def printStudentAge(self, name):
        """Prints the age of student"""
        for i in range(len(self.studentList) - 1):  # Find the index of student's age
            if self.studentList[i] == name:
                break
        print(self.studentList[i].age)


class Student:
    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age

    def printStudentName(self):
        """Prints the name of student"""
        print(self.name)

    def printStudentLastName(self):
        """Prints the name of student"""
        print(self.lastName)



school1 = School("Elementary", "Toronto", 300)
school2 = School("Secondary", "Toronto", 500)

student1 = Student("Max", "Smith", 8)
student2 = Student("Bob", "Patel", 10)
student3 = Student("Alice", "Kim", 16)
student4 = Student("Sara", "William", 17)
student5 = Student("Ross", "Long", 16)

school1.addStudentToSchool(student1, student2)
school2.addStudentToSchool(student3,student4,student5)

school2.printStudentAge("Sara")

for i in school2.studentList:
    print(i.age)

# Structure of a class
"""
class className:
    classVariable1 =...
    classVariable2 = ...
    def __init__(self, objectParameter1, objectParameter2,...):
        self.variable1 = ...
        self.variable2 = ...

    def otherMethods(self, parameter1, parameter2, ...):
        ...
    def evenAnotherMethod(self, parameter1, parameter2, ...):
        ...

someObject = className(argument1, argument2)
"""
# Example 2
class Circle:
    pi = 3.1415    # Static variable, it is the same for ALL objects

    # The constructor. It accepts the radius of the object
    def __init__(self, radius):
        """
        The non-static variable is called radius.
        We must assign any argument passed while constructing the object
        to the non-static variable so it can be used later.
        """

        self.radius = radius

    # Calculates and prints the area of the object
    def printArea(self):
        """
        To use the static variable, className.variable syntax should be used.
        To use the non-static variable, self.variable syntax should be used.
        """
        area  = Circle.pi * (self.radius)**2
        print(area)

circle1 = Circle(10)
circle2 = Circle(6)
circle1.printArea()
circle2.printArea()

# Example 3 -- accessing attributes

circle1Radius = circle1.radius
circle2Radius = circle2.radius
print(f"""
Circle1 radius: {circle1Radius}
Circle2 radius: {circle2Radius}
""")

# Example 4 -- Changing value of an attribute
circle1.radius = 100
print(f"Circle 1 radius: {circle1.radius}")

# Example 5 -- Changing value of an attribute, a better way
class Circle:
    pi = 3.1415

    def __init__(self, radius):
        self.radius = radius

    def printArea(self):
        area  = Circle.pi * (self.radius)**2
        print(area)

    # This function will print the radius of the circle
    def printRadius(self):
        print(self.radius)

    # This function will change the radius of the circle
    def changeRadius(self, newRadius):
        self.radius = newRadius

circle1 = Circle(10)
circle1.printRadius()

circle1.changeRadius(100)
circle1.printRadius()

# Example 6
class Car:
    count = 0
    def __init__(self, model, color, initialXLocation):
        self.color = color
        self.model = model
        self.xLocation = initialXLocation
        Car.count += 1

    def move(self, moveBy):
        """Change car's location by the given value"""
        self.xLocation += moveBy

    def printInfo(self):
        """Print car's info"""
        print(f"""
        Model = {self.model}
        Color = {self.color}
        X Location = {self.xLocation}
        """)

    # def __str__(self) -> str:
    #     return f"""
    #     Model = {self.model}
    #     Color = {self.color}
    #     X Location = {self.xLocation}
    #     """


car1 = Car("BMW", "Black", 0)
print(f"Total car created: {Car.count}")
car2 = Car("Mercedes", "White", -10)
print(f"Total car created: {Car.count}")

car1.printInfo()
car2.printInfo()

print(f"Total car created: {car1.count}")
print(f"Total car created: {car2.count}")

# Moving the cars
car1 = Car("BMW", "Black", 0)
car2 = Car("Mercedes", "White", -10)

car1.move(-50)
car1.move(15)
car1.move(8.5)

car2.move(12.6)
car2.move(-8.7)

car1.printInfo()
car2.printInfo()

# Example 7 -- collections
myList = [car1, car2]   # List of Cars
myList = [car1, circle1, 25, "text"]    # List of various data types


# Example 8

print(f"Car1: {car1}")
print(f"Car2: {car2}")
print(f"circle1: {circle1}")
print(f"circle2: {circle2}")


# Example 9 -- __str__() method
class Car:
    count = 0
    def __init__(self, model, color, initialXLocation):
        self.color = color
        self.model = model
        self.xLocation = initialXLocation
        Car.count += 1

    def move(self, moveBy):
        """Change car's location by the given value"""
        self.xLocation += moveBy

    def __str__(self):
        return f"""
        Model = {self.model}
        Color = {self.color}
        X Location = {self.xLocation}
        """


car1 = Car("BMW", "Black", 0)
car2 = Car("Mercedes", "White", -10)

print(car1)
print(car2)

# Example 10

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addVectors(self, other):
        # This makes sures that the other object is a Vector
        if type(other) == type(self):
            newx = self.x + other.x
            newy = self.y + other.y
            newz = self.z + other.z
            return Vector (newx, newy, newz)

        else:
            print("Wrong operation")

    def __str__(self):
        return f"""
        x: {self.x}
        Y: {self.y}
        Z: {self.z}
        """

vector1 = Vector(5,0,0)
vector2 = Vector(0,10,0)
vector3 = vector1.addVectors(vector2)

print(vector3)


# Example 11
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if type(other) == type(self):
            newx = self.x + other.x
            newy = self.y + other.y
            newz = self.z + other.z
            return Vector(newx, newy, newz)

        else:
            print("Wrong operation")

    def __str__(self):
        return f"""
        x: {self.x}
        Y: {self.y}
        Z: {self.z}
        """


vector1 = Vector(5,0,0)
vector2 = Vector(0,10,0)
vector3 = vector1 + vector2

print(vector3)

# Example 12
myList = [1,2,3]
myList.append(12)   # Add to the end of the list
myList.clear()      # Remove all elements of the list
newList = myList.copy()     # Create a new list with the same elements and return it


# Example 13 -- The very first Game
class Player:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0


    def moveX(self, xValue):
        self.x += xValue

    def moveY(self, yValue):
        self.y += yValue

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Game:
    def __init__(self, name, player, canvasSize = 20):
        self.player = player
        self.name = name
        self.canvasSize = canvasSize
        self.player.x = canvasSize//2
        self.player.y = canvasSize //2


    def render(self):
        # This method renders the game on the screen.
        for i in range(self.canvasSize + 1):
            for j in range(self.canvasSize + 1):
                if i == 0 or i == self.canvasSize  \
                        or j ==0 \
                        or j == self.canvasSize:

                    print("#", end = "")

                elif i == self.player.getY() and j == self.player.getX():
                    print("X", end = "")

                else:
                    print(" ", end ="")

            print("\n", end = "")



    def run(self):
        play = True
        print("""
        You need to move the player to the edge of the map 
        to finish the game.
        
        To go Left press: l
        To go Right press: r
        To go Up press: u
        To go Down press: d
        To Exit press: e
        
        """)
        # The loop continues until the player has reached
        # the edge of the map.
        while play:
            print(f"{self.name} played by {self.player.name}")
            self.render()
            # This ensures that game only moves forward
            # if the write key is pressed
            while True:
                # Change the character to lower case for easy comparison
                userInput = input("Your move: ").lower()
                if userInput == "l":
                    self.player.moveX(-1)
                    break
                elif userInput == "r":
                    self.player.moveX(1)
                    break
                elif userInput == "u":
                    self.player.moveY(-1)
                    break
                elif userInput == "d":
                    self.player.moveY(1)
                    break
                elif userInput == "e":
                    play = False
                    break
                else:
                    print("invalid input, please try again")

            # Check if the x_axis has reached either left or right
            if self.player.getX() == 0 \
                    or self.player.getX() == self.canvasSize:
                play = False
            # Check if the y_axis has reached either up or down
            if self.player.getY() == 0 \
                    or self.player.getY() == self.canvasSize:
                play = False

        print("Game Over.")

player = Player("Raman")
game = Game("Puzzle", player)
game.run()

