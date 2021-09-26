# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phoneBook = {}
for i in range(n):
    l1 = list(map(str, input().split()))
    key = l1[0]
    value = l1[1]
    phoneBook[key] = value
    
    
while True:
    try:
        name = input()
        if name in phoneBook:
            print(name + "=" + phoneBook[name])
        else:
            print("Not found")
    except:
        break
