# Datatype

number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
is_Python_Interesting = True  # bool

# A variable with multiple values
languages = ["python", "php", "java", "kotlin"]  # list
fuits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "Ghana", "China"}  # Set
# Dictionary
details = {
    "firstname" : "Ashley",
    "course" : "MIT",
    "age" : 18,
    "nationality" : "American"
}
print(details["firstname"])
print(details["nationality"])
print(number)
print(num)
print(greeting)
print(is_Python_Interesting)
print(countries)

# Determining the data type of variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - Converting one data type to another
print(float(number))
print(int(num))
