
ans="1101"
zero=0
one=0
d={}
for i in ans:
    if i=="0":
        zero+=1
        d["Zeros"]=zero
    else:
        one+=1
        d["Ones"]=one
print(d)

a=dict(name     ="Junaid Ali",
       age      ="17",
       city     ="sukkur",
       caste    ="soomro",
       address  ="BISE")
n=input("Enter name,age,city,caste,address :")
if n=="name":
    print("His name is",a[n])
elif n=="age":
    print("His age is",a[n])



months = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}

n=int(input("Enter Value to Get KEY : "))
for i in months:
    if i==months[n]:
        print(i)

#PRINT JUST KEYS
print("Just keys :")
for i in months :
    print(i,end=" ")

print()
print ("Months and numbers are : ")
for i in months :
    print(i, months[i], end=" ")

months = {1:"Jan",2:"Feb",3:"Mar",4:"April",5:"May",6:"June",7:"July",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
for i in months:
    print(i,"\t", months[i])

a=int(input("Enter first month : "))
b=int(input("Enter second month : "))

dist = b - a

print(months[a],"and",months[b],"are", dist, 'months apart.')

A=["10","11","12","13","14","15"]
dic1={"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
for j in A:
    print(dic1[j],end=" ")
