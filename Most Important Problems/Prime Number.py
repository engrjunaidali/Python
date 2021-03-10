# With for Loop

num=int(input("Enter number: "))
for i in range(2,num):
    if num%i==0:
        print("This is not a Prime Number")
        break
else:
    print("This is a Prime Number")

# With while loop

# num=int(input("Enter Number: "))
i=2
isprime=0
while num%i==0 and i<num:
    isprime=1
    i+=1
if isprime==1:
    print("Not Prime")
else:
    print("Prime")
