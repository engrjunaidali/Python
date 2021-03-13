open("csit.txt","w")
file=open("csit.txt","w")
print(file)

file.write("XYZ")
file.write("ABC")

file=open("csit.txt","a")
file.write("\nJunaid Ali SOomro")
file.write("\nWEEK13")
file.write("\nThirteen")
file.write("\nPakistan")
file.write("\nZindabad")

file=open("csit.txt","r")
# print(file.read())                      #Read entire doc
# print(file.read(6))                     #Read six letters
# print(file.readline())                  #Read 1st line
print(file.readline())                  #Read 2nd line
print(file.readline(2))                 #Read two letters in line

print(file.readlines())                 #Read lines into list

file=open("csit.txt","r")
for i in file:
    print(i)

#PRINT 2nd LINE
i=1
file=open("csit.txt","r")
for x in file:
    if i==2:
        print(x)
    i+=1

#COPY PASTE FILE
file=open("csit.txt","r")
ftp=open("neduet.txt","w")
for x in file:
    ftp.write(x)
file.close()
ftp.close()