# While loop
# Incrementing a value
number = 5
while number <= 10:
    print(number)
    number += 1

# Decrementing a value
num = 105
while num >= 100:
    print(num)
    num -= 1

# Break Statement
x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x += 1

# Continue Statement
count = 19
while count < 25:
    count += 1
    if count == 23:
         continue
    print(count)

# For loop
languages = ["Python", "C++", "Kotlin"]
for lang in languages:
    print(lang)

# Range
for z in range(6):
    print(z)

for y in range(20, 31):
    print(y)

for i in range(30, 41, 2):
    print(i)

for inno in "Innovators":
    print(inno)


