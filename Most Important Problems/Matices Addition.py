n=int(input("Enter no. of rows or columns : "))
A=[]
B=[]
for x in range(2):                                  #no of matrices
    for i in range(n):                              #no of rows and columns
        mylist=[]
        for j in range(n):
            print(1+i,1+j,end=" ")
            if x==0:                                #Single row of matrix
                temp=int(input("Enter Number for list A : "))
                mylist.append(temp)
            if x==1:
                temp = int(input("Enter Number for list B : "))
                mylist.append(temp)
        if x==0:
            A.append(mylist)
        elif x==1:
            B.append(mylist)

print("A=",A)
print("B=",B)

C=[]
for i in range(n):
    tlist=[]
    for j in range(n):
        x=0
        tlist.append(x)
    C.append(tlist)

for i in range(len(A)):
    for j in range(len(A)):
        C[i][j] = A[i][j] + B[i][j]
print("C=",C)


# my_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
# # How many elements each
# # list should have
# n = 4
#
# # using list comprehension
# final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n)]
# print(final)
