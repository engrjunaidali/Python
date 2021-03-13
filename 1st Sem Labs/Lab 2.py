"""
Lab 2.1
Write a script that take user input for a number
then adds 3 to that number.
Then multiplies the result by 2, subtract 4, then again adds 3,
then print the result.
"""

n=int(input("Enter Number : "))
n=((((n+3)*2)-4)+3)
print(n)


# Lab 2.2
# Write a script that takes input as radius then calculate area of circle.
r=int(input("Enter Radius : "))
print("Area is : ",(22/7)*r**2)

# Lab 2.3
# Write a Python program to take user input and then calculate the sum of three given numbers
a=int(input("Enter first no : "))
b=int(input("Enter second no : "))
c=int(input("Enter third no : "))
sum=a+b+c
print(sum)

# Lab 2.4
# Write a script that print first and last name in reverse order with a space between them
a=input("Enter first name : ")
b=input("Enter second name : ")
print("Hello",b,a)