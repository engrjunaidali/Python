# Lab 9.1 Swap the elements of two lists without using temp list

A=[]
B=[]
num=int(input("How many numbers you will enter : "))
for i in range(2):
    for j in range(num):
        if i==0 :
            n=int(input("Enter Number for list A : "))
            A.append(n)
        if i==1:
            o=int(input("Enter Number for list B : "))
            B.append(o)
print("printing A: ",A)
print("printing B: ",B)
print()
for i in range(len(A)):
    A[i]=A[i]+B[i]
    B[i]=A[i]-B[i]
    A[i]=A[i]-B[i]
print("printing A: ",A)
print("printing B: ",B)
                                    #B=A-B
                                    #A=A-B

# Lab 9.2

A=[]
n=int(input("How many numbers : "))
for i in range(n):
    x=int(input("Enter number : "))
    A.append(x)

print("before sorting\t",A)

for i in range(len(A)-1,0,-1):
    for j in range(i):
        if A[j]>A[j+1]:
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp
print("after sorting\t",A)