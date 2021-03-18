n=5
for i in range(n):
    for j in range(n):
        if (i==0 and j==0) or (i==n-1 and j==0):
            print(end="  ")
        elif i==0 or j==0 or i==n-1 or (j==n-1 and i>n//2) or (i==n//2 and j>n//2) or (i==n//2 and j==n//2 ) or (j==n//2 and i==n//2+1):
            print("*", end=" ")
        else:
            print(end="  ")
    print()

n=5


# for Q
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n//2 or (j==n-1 and i<n//2) or (i==j and i>n//2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# for i in range(n):
#     for j in range(n):
#         # if j==i-n//2 or j==n//2-i:
#         if j==i-n//2:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==n//2 and j==n//2 or j==n//2 and i==n//2+1:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
print()

n=5
# for S
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or i==n//2 or (j==0 and i<n//2) or (j==n-1 and i>n//2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# For W
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or (i+j==n-1 and i>n//2) or (i==j and i>n//2) or (i==n//2 and j==n//2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
# for Q
# for i in range(n):
#     for j in range(n):
#         if (j==0 ) or (i==0) or j==n-1 or i==n-1 or i==j and i+j==n-1 or i==j and i>n//2:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
# for J

for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or (i==n-2 and j==0) or (i==n-1 and j<n//2) :
            print("*",end=" ")
        else:
            print(end="  ")
    print()