print("1\t2\t3\t4\nA\tB\tC\tD\nE\tF\tG\tH\nI\tJ\tK\tL\nM\tN\tO\tP\nQ\tR\tS\tT\nU\tV\tW\tX\nY\tZ")

list=[["A","E","I","M","Q","U","Y"],
      ["B","F","J","N","R","V","Z"],
      ["C","G","K","O","S","W"],
      ["D","H","L","P","T","X"]]

n=int(input("Number of letters in the word : "))

A=[]
for i in range(n):
    t=int(input("Enter Col "+ str(i+1) +" : "))
    A.append(list[t-1])
print()

print("1\t2\t3\t4\t5\t6\t7")

for i in range(len(A)):
    for j in A[i]:
        print(j, end="\t")
    print()
print()

B=""
for j in range(n):
    p=int(input("Enter Col "+ str(j+1) +" : "))
    B+=A[j][p-1]

print("\nI think the word you are guessing is : ",end="")
print(B)
