str = input("Enter string : ")

print(str)


def convert(str):
    a = ""
    for i in str:
        if i == "a" or i == "b" or i == "c":
            a = a + "2"
        if i == "d" or i == "e" or i == "f":
            a = a + "3"
        if i == "g" or i == "h" or i == "i":
            a = a + "4"
        if i == "j" or i == "k" or i == "l":
            a = a + "5"
        if i == "m" or i == "n" or i == "o":
            a = a + "6"
        if i == "p" or i == "q" or i == "r" or i == "s":
            a = a + "7"
        if i == "t" or i == "u" or i == "v":
            a = a + "8"
        if i == "w" or i == "x" or i == "y" or i == "z":
            a = a + "9"
    return a

print(convert(str))