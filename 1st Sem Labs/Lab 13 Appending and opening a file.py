n=int(input("Enter Number Of Employees: "))
A=[]
for i in range(n):
    temp=[]
    id=input("Enter ID : ")
    name=input("Enter Name : ")
    salary=input("Enter Salary : ")
    temp.append(id)
    temp.append(name)
    temp.append(salary)
    A.append(temp)

file=open("employee.txt","wt")
for files in A:
    file.write("\nID : "+files[0]+"\nName : "+files[1]+"\nSalary : "+files[2])

try:
    file=open("employee.txt","rt")
    print(file.read())
except FileNotFoundError:
    print("FILE NOT FOUND")
else:
    file.close()

#OR
a=int(input("Enter Employee Number : "))
file=open("employee.txt","wr")
for i in range(a):
    id=input("ID : ")
    name=input("Name : ")
    salary=input("Salary : ")
    file.write("\nID : "+id+"\nName : "+name+"\nSalary : "+salary)
file.close()

# file=open("employee.txt","r")
print(file.read())