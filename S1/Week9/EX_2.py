x = int(input())

data = []
for _ in range(x) :
    data.append(input())

data.sort()
print(data)
data.sort(reverse=True)
print(data)
