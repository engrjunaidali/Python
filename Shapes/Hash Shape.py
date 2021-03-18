n=5


print(a(2))


def call():
    print(" * ",end="")
#Hash
for i in range(n):
    for j in range(n):
        if i%2!=0 or j%2!=0:
        # if i%2==0 or j%2==0:
        # if i==0 or j==0:
            call()
        else:
            print(end="   ")
    print()
print()


