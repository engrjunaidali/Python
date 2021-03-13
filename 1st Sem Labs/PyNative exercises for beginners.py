#Exercise of site
#https://pynative.com/python-basic-exercise-for-beginners


#Question 1: Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum
m=int(input("Enter Number: "))
n=int(input("Enter Number: "))
r=m*n
if r>1000:
    print(m+n)
else:
    print(r)

#Question 2: Given a range of numbers.
# Iterate from o^th number to the end number and print the sum of the current number and previous number.

n=int(input("Enter Number for fibonnica series : "))
a=0
b=1
for i in range(n):
    if i == 0:
        print("0")
    else:
        c=a+b
        a=b
        b=c
        print(c)

#Question 3: Accept string from the user
# and display only those characters which are present at an even index
str = "pynative"
for i in range(len(str)):
    if i%2==0:
        print(str[i])

#Question 4: Given a string and an int n,
# remove characters from string starting from zero up to n and return a new string

def remove(n):
    return str[n:]

str=input("Enter string : ")
n=int(input("Enter Index : "))
print(remove(n))

#Question 5: Given a list of ints, return True if first and last number of a list is same

n=int(input("How many numbers you will enter into list : "))
A=[]
for i in range(n):
    a=int(input("Enter Number : "))
    A.append(a)

if A[0]==A[-1]:
    print("First and last number is same")

#Question 6: Given a list of numbers,
# Iterate it and print only those numbers which are divisible of 5

n=int(input("How many numbers you will enter into list : "))
A=[]
for i in range(n):
    a=int(input("Enter Number : "))
    A.append(a)

for j in A:
    if j%5==0:
        print(j,end=" ")

#Question 7: Return the number of times that the string appears anywhere in the given another string

n=input("Enter phrase that repeats the words : ")
r=input("Enter repeated word : ")
c=0
n=n.split()
for i in n:
    if i in r:
        c+=1
print(c)

#Question 8: Print the following pattern

n=int(input("Enter Number of rows :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>j or i==j:
            print(i,end="")
        else:
            print(end="")
    print()


#Question 9: Reverse a given number and return true
# if it is the same as the original number

n=input("ENter Number : ")
if n==n[::-1]:
    print(n)

#Question 10: Given a two list of ints create a third list
# such that should contain only odd numbers from the first
# list and even numbers from the second list
#Merged List is     [23, 11, 17, 24, 36, 12]

A = [10, 20, 23, 11, 17]
B = [13, 43, 24, 36, 12]
C=[]
for i in A:
    if i%2==1:
        C.append(i)
for j in B:
    if j%2==0:
        C.append(j)
print(C)