string=input("ENTER NAME : ")
string.lower()
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels=vowels+1
print("Number of vowels are: ",vowels)


#
# name=input("Enter Name: ")
# name.lower()
# v=0
# c=0
# for i in name:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#             v+=1
#       else:
#             c+=1
# print("V O W E L S : ",v)
# print("C O N S O N E N T S : ",c)


name=input("ENTER NAME : ")
name.lower()
c=0
v="aeiou"
for x in name:
      if x in v:
            c+=1
print(c)