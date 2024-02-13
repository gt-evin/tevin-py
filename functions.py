# Inbuilt Functions
y = max(67, 56, 34, 23, 89)
print(y)

x = min(12, 34, 56, 1, 79)
print(x)

z = pow(2, 3)
print(z)


# User-defined Functions
def details():
    print("Tevin")


details()  # Calling a function


# Parameters and arguments
def students(name, course, age):
    print(name, course, age)


students("Ashley", "MIT", 17)
students("Goretty", "CuberSecurity", 19)


# Fullname, Idno, Salar, Position, Age
def employees( Fullname, Idno, Salary, Position, Age):
    print(Fullname, Idno, Salary, Position, Age)

employees("George Tevin", 32589,  370000, "Managing Partner", 38)
employees("Hailee Kerubo", 188309, 300000, "Senior Partner", 44)
employees("Lucy Washuka", 45678,  295000, "Chief of staff", 30)
employees("Miles Brown", 32498,  100000, "Civil operator", 26)
employees("Jack Daniels", 32498,  67000, "Janitor", 20)


