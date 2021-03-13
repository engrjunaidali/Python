# Lab 5.1

name="junaid ali"
print(name.title())
print(name.upper())
print(name.lower())

# Lab 5.2

name=input("Enter Your name : ")
n=input("Enter letter to know index : ")
name=name.find(n)
print(name)

# Lab 5.3

name=input("Enter Name : ")
n=int(input("Enter Number : "))
print(name.lower()[:n]+name.upper()[n:])

# Lab 5.4

# Write a Python program that asks users for their favourite color.
# Create the following output
# (assuming blue is the chosen color)
# (hint: use ‘+’ and ‘*’)
# blueblueblueblueblueblueblueblueblueblue

colour=input("Enter colour : ")
colour=(colour*2+colour*8)
print(colour)
