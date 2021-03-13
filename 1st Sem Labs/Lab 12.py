# Lab 12.1

data=50
try:
    data=data/0
except ZeroDivisionError:
    print("Cannot divide by 0", end="")
else:
    print("Divison Successful", end="")
print()
try:
    data=data/5
except:
    print("Inside Except Block", end="")
else:
    print("GFG", end="")

print("\n")

#program 2
value=[1,2,3,4]
data=0
try:
    data=value[0]
except IndexError:
    print("CSIT Index Error", end="")
except:
    print("NEDUET Index Error", end="")
finally:
    print("Python Index Error", end="")

data=10
try:
    data=data/0
except ZeroDivisionError:
    print("CSIT ZeroDivisionError", end="")
finally:
    print("Python ZeroDivisionError")

x=-1
if x<0:
    raise Exception ("Number is below 0")