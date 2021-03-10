n=int(input("Enter Number: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i<=j:
            print("*",end="")
        else:
            print(end=" ")
    print()

num=5
for i in range(num+1):
    for j in range(i):
        print("#", end="")
    print()

for i in range(num+1):
    for j in range(num-i):
        print("#",end="")
    print()

i=1
while i<5:
    j=1
    while j<=i:
        print("X",end="")
        j=j+1
    print("")
    i=i+1

n=5
i=1
while i<=n:
    j=n
    while i<=j:
        print("*",end="")
        j-=1
    print(" ")
    print(" "*i,end="")
    i+=1
