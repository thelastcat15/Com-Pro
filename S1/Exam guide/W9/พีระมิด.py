a = int(input())
for i in range(a-1):
    for j in range(i):
        print("+",end = "")
    print("")
for i in range(a):
    for j in range(a-i-1):
        print("+",end = "")
    print("")
