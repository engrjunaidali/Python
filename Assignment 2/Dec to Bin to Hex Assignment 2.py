dec=int(input("Enter Numbre in Decimal : "))
# dec=154
binn=""
while dec>0:
    b=dec%2
    binn=str(b)+binn
    dec//=2
# print(binn)
l=len(binn)

A=[]
i=0
while i < len(binn):
    j=0
    temp=[]
    for j in range(4):
        temp.append(binn[i])
        if i == len(binn)-1:
            break
        else:
            i+=1
    A.append(temp)
print(A)


# A=[]
# m=l%4
# l=l//4+m
# for i in range():
#     temp=[]
#     for j in range(4):
#         temp.append(0)
#     A.append(temp)
# print(A)



# a=[]
# for i in range(len(binn)):
#     temp=[]
#     for j in range(4):
#         temp.append(0)
#     a.append(temp)
# print(a)

#
# for i in binn:
#     a.append(i)
# print(a)


#                                         #Converting Decimal to Binary
# a=[]
# def dtb(num):
#     if num>1:
#         dtb(num//2)
#     a.append(num%2)
# n=int(input("Enter number: "))
# dtb(n)
#                                         #inserting Zero to the left to complete the bits
# for i in range(100):
#     if len(a)%4!=0:
#         a.insert(0,0)
#
#                                         #Dividing the list in 4 element chunks
# def divide_chunks(l, n):
#     # looping till length l
#     for i in range(0,len(l), n):
#         yield l[i:i + 4]
#     # How many elements eac12h
# n = 4                                       # list should have 4 digit chunks
# x = list(divide_chunks(a, n))
# # print(x)
#
# l=len(x)
# sum1=0
# sum2=0
# sum3=0
# sum4=0
# sum5=0
# for i in range(l):
#     for j in range(4):
#         for k in str(x[i][j]):
#             if i==0 and k=="1":
#                 sum1=sum1+2**(3-j)
#                 break
#             if i==1 and k=="1":
#                 sum2=sum2+2**(3-j)
#                 break
#             if i==2 and k=="1":
#                 sum3=sum3+2**(3-j)
#                 break
#             if i==3 and k=="1":
#                 sum4=sum4+2**(3-j)
#                 break
#             if i==4 and k=="1":
#                 sum5=sum5+2**(4-j)
#                 break
#
# A=[sum1,sum2,sum3,sum4,sum5]
# dic1={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
# ans=""
# for i in A:
#     if i==0:
#         continue
#     if i>9:
#         ans+=dic1[i]
#     else:
#         ans+=str(i)
# print(ans)



