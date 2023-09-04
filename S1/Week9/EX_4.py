x = int(input())

for _ in range(x) :
    x.append(int(input()))

if int(input()) in x :
    print("MEET")
else :
    print("MISS")