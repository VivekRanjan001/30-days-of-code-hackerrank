value = int(input())
for z in range(value):
    strr = input()
    strlist = list(strr)
    for i in range(len(strlist)):
        if i%2 == 0:
            print(strlist[i],sep = "-",end="")
    print(" ",end="")
    for i in range(len(strlist)):
        if i%2 != 0:
            print(strlist[i],end="")
    print()
