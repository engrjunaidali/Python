n=5
i=0
while i<=n:
    print(" * "*(n-i)+" "*i)
    i+=1

n=5
i=0
while i<=n:
    print(" * "*(i)+" "*(n-i))
    i+=1

n=5
i=0
while i<=n:
    print(" "*(n-i)," *"*(i))
    i+=1

#dec to binary
n=13
binn=""
while n>0:
    b=n%2
    binn=str(b)+binn
    n=n//2
print(binn)



# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return n,"is not a PRIME number."
#             break
#     else:
#         return n,"is PRIME number."
#
# for i in range(2,100):
#     print(prime(i))
a=1
while a==1:
    n=input("Enter : ")
    print(n[::-1])
    a=int(input("press 1 for once again..."))
