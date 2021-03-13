import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nedian",
    database="prime")

mycursor=mydb.cursor()
n=int(input("Enter Number : "))

for i in range(2,n):
    if n%i==0:
        print("It is not a prime.")
        break
else:
    print("It is a prime.")

try:
    mycursor.execute("CREATE DATABASE prime")
    mycursor.execute("CREATE TABLE numbers(pnumbers int(10),)")

except:
    mycursor.execute("SELECT * FROM numbers")
    result=mycursor.fetchall()
    c=0
    for i in range(len(result)):
        for j in result[i]:
            if n==j and c==0:
                print(j, "is already stored in database.",end="")
                c=1
                break
    if c!=1:
        mycursor = mydb.cursor()
        sql = "INSERT INTO numbers (pnumbers) VALUES (%s)"
        val = [ (n) ]
        mycursor.execute(sql, val)
        mydb.commit();
        print(mycursor.rowcount, "was inserted.")



# for i in result:
#
#     for j in a:
#         if n==i:
#             print(i)


        # mycursor.execute(" SELECT * FROM numbers ")
        # print(mycursor.fetchone())
#     else:
#         for j in range(2,n):
#             if n%j==0:
#                 print("NOT PRIME")
#                 break
#         else:
            # mycursor = mydb.cursor()
            # sql = "INSERT INTO numbers (pnumbers) VALUES (%s)"
            # val = [ (n) ]
            # mycursor.execute(sql, val)
            # mydb.commit();
            # print(mycursor.rowcount, "was inserted.")
# #
# for i in range(2,n):
#     if n%i==0:
#         print("NOT PRIME")
#         break
# else:
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM numbers")
#     result=mycursor.fetchall()
#     for i in result:
#         print(i)
#         if i == n:
#             mycursor.execute("SELECT * FROM numbers")
#             print(mycursor. fetchone())
#         else:
#             mycursor = mydb.cursor()
#             sql = "INSERT INTO numbers (pnumbers) VALUES (%s)"
#             val = (n)
#             mycursor.execute(sql, val)
#             mydb.commit();
#             print(mycursor.rowcount, "was inserted.")
#
#
#
#
