from fractions import Fraction
A=[]
# n=int(input("2x2 or 3x3 : "))
n=3
a=0
for i in range(n):
    B=[]
    for j in range(n):
        a+=i+j
        # print(i+1,j+1,end=" ")
        # a=int(input("Enter Number : "))
        B.append(a)
    A.append(B)
print(A)

B=[]
B.append(A)
C=[]
if n == 2 :
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if det == 0 :
        print("Inverse doesn't exist as d=0")
    else:
        print("Determinant is : ",det)
        a=Fraction(A[0][0]/det)
        b=Fraction(A[0][1]/det)
        c=Fraction(A[1][0]/det)
        d=Fraction(A[1][1]/det)
        inv = [[d, -b],
               [-c, a]]
        print("Inverse of 2x2 is :",inv)

def mat(m):
     return m[0][0] * m[1][1] - m[0][1] * m[1][0]
if n==3:

    a=[i[1:] for i in A[1:]]
    b=[j[::2] for j in A[1:]]
    c=[k[:2] for k in A[1:]]
    d=[l[1:] for l in A[::2]]
    e=[m[::2] for m in A[::2]]
    f=[n[:2] for n in A[::2]]
    g=[o[1:] for o in A[:2]]
    h=[p[::2] for p in A[:2]]
    i=[q[:2] for q in A[:2]]

    det=A[0][0]*mat(a)-A[0][1]*mat(b)+A[0][2]*mat(c)
    if det==0:
        print("Inverse doesn't exist as det=",det)
    else:
        print("Determinant :",det)
        a = Fraction(mat(a),det)
        b = Fraction(mat(b), det)
        c = Fraction(mat(c), det)
        d = Fraction(mat(d), det)
        e = Fraction(mat(e), det)
        f = Fraction(mat(f), det)
        g = Fraction(mat(g), det)
        h = Fraction(mat(h), det)
        i = Fraction(mat(i), det)


        inv=[[a,-d,g],[-b,e,-h],[c,-f,i]]
        # print("Inverse is : ",inv)
        for i in inv:
            print(i)
        # print("[",a,"\t",-d,"\t",g,"\t\t]\n[",-b,"\t",e,"\t",-h,"\t]\n[",c,"\t",-f,"\t",-i,"\t]")

        # print("a : ", a)
        # print("b : ", b)
        # print("c : ", c)
        # print("d : ", d)
        # print("e : ", e)
        # print("f : ", f)
        # print("g : ", g)
        # print("h : ", h)
        # print("i : ", i)