# Lab 10.1 minn and maxx value in TUPLE

A=[]                                                    #Appending numbers into list
n=int(input("How many numbers you will enter : "))
for i in range(n):
        x=input( "Enter Number : ")
        A.append(x)
A=tuple(A)




minn=A[0]
for x in A:
        if x<minn:      minn=x
        if x>minn:      maxx=x
print("minimum is ",minn ," and maximum is ",maxx)

# Lab 10.2

#To count the letters in Dictionary

n=input("Enter Name : ")

A=[]
for i in n:
        A.append(i)
print(A)

dict1={}
for ltr in A:
    if ltr in dict1:    dict1[ltr] += 1
    else:               dict1[ltr] = 1
print(dict1)


#To count the words in dictionary
string=input("Enter Name : ")
mystring = string.lower().split()
dict1 = {}
for item in mystring:
    if item in dict1:   dict1[item] += 1
    else:               dict1[item] = 1
print(dict1)

