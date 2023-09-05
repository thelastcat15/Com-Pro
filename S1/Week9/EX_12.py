x = int(input())

data = []
for _ in range(x) :
    data.append(int(input()))

avg = sum(data) / x

upper = 0
for i in data :
    upper += (i - avg) ** 2

ans = (upper / (x-1)) ** 0.5
print(ans)