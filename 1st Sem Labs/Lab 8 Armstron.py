# Lab 8.1 Armstrong

#Simple Logic For Checking Armstrong

n=int(input("Enter Number: "))
l=len(str(n))
orig=n
sum=0
while n>0:
    sum=sum+(n%10)**l
    n=n//10
if orig==sum:
    print("Amstrong")
else:
    print("not Amstrong")

# def check_armstrong(n):
#     l=len(str(n))
#     sum=0
#     while n>0:
#         sum=sum+(n%10)**l
#         n=n//10
#     return sum
# n=int(input("Enter Number : "))
# a=check_armstrong(n)
# if n==a:
#     print("Armstrong Number")
# else:
#     print("Not Amstrong Number")

# Munchausen numbers
# while n>0:
#     sum=sum+(n%10)**(n%10)                    #3435,
#     n=n//10









