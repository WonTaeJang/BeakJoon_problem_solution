var1, var2 = input().split()
var1 = int(var1)
var2 = int(var2)

if var1 > var2:
    print(">")
elif var1 < var2:
    print("<")
else:
    print("==")