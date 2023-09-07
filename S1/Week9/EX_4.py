x = int(input())

data = []
for _ in range(x) :
    data.append(int(input()))

if int(input()) in data :
    print("MEET")
else :
    print("MISS")