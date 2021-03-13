import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="nedian",
	database="ASIFSTORE")

mycursor=mydb.cursor()
# mycursor.execute("create database ASIFSTORE")
# mycursor.execute("show databases")
# for i in mycursor:
# 	print(i)
mycursor.execute("CREATE TABLE customers(name VARCHAR(255),city VARCHAR(255))")
