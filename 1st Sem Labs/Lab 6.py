# Lab 6.1

# Write a program that generate square of 1 to 10 numbers (using for loop).

for i in range(1,11):
    print(i,"\t=\t",i*i)


# Lab 6.2

#Write a program that take a user input and to create the multiplication table
# (from 1 to 10) of that number.

n=int(input("Enter Number : "))
for i in range(1,11):
    print(i,"\tX\t",n,"\t=\t",i*n)

# ALTERNATIVE
i=1
while i<=10:
    print(str(n)+"\tX\t"+str(i)+"\t=\t"+str(i*n))
    i=i+1

# Lab 6.3 FIBONNICA SERIES

x=int(input("Enter Number : "))
a,b=1,1
if x==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,x):
        c=a+b
        a=b
        b=c
        print(c)

# Lab 6.4

                #Numbers Triangle
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1


