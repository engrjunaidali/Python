ans=""
n=int(input("Enter Number  : "))
if n>=0:
    ans=1
    while n>1:
        ans=ans*n
        n-=1
if ans>0:
    print(ans)
else:
    print("Positive Needed")

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("Enter Number : "))
print(fact(n))

for i in range(1,10):
    print(i,fact(i))


# #Factorial in def function
#
def fact(x):
    if x>=0:
        ans=1
        while x>1:
            ans=ans*x
            x=x-1
        return ans
n=int(input("#"))
num=fact(n)
if num!=None:
    print(num)
else:
    print("+ve Needed")
#
# #Simple Logic of Factorial
ans=""
n=int(input("Enter Number  : "))
if n>=0:
    ans=1
    while n>1:
        ans=ans*n
        n-=1
if ans>0:
    print(ans)
else:
    print("Positive Needed")


