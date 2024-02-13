temperature = 32

if temperature > 37:
    print("It is hot")
else:
    print("It is cold")

# A program that prints out the largest number among three numbers
num1 = 45
num2 = 85
num3 = 22
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number ")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 0
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether a number is prime or not
n = 5
if n>1:
 for i in range(2,n//2):
     if(n%1)==0:
         print(n,"is not a prime number")
     break
 else:
    print(n,"is a prime number")
else:
    print(n,"is neither prime nor composite")

