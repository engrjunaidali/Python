# Program to multiply two matrices using nested loops
# 3x3 matrix
A = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x3 matrix
B = [[5,8,1],
    [6,7,3],
    [4,5,9]]
# result is 3x3
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]
# iterate through rows of X
for i in range(len(A)):
   # iterate through columns of Y
   for j in range(len(B[0])):
       # iterate through rows of Y
       for k in range(len(B)):
           C[i][j] += A[i][k] * B[k][j]
for r in C:
   print(r)