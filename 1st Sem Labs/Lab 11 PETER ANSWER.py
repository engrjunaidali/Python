from msvcrt import getch

print("Petition : ", end="")
A = ""
x = ["A", "n", "s", "w", "e", "r", " ", "m", "e", " ", "p", "l", "e", "a", "s", "e"]  # 15 chr
i = 0
while i <= len(x):
    a = getch().decode()
    if a == ".":
        print(x[i], end="")
        i += 1
        while i < len(x):
            b = getch().decode()
            if b != ".":
                print(x[i], end="")
                A += b
                i += 1
            else:
                print(x[i], end="")
                i += 1
                break
    else:
        print(a, end="")
        i += 1
input("Your Question : ", end="")
print(A)
