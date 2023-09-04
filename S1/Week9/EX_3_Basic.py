x = int(input())

sum = 0
data = []
for _ in range(x) :
    temp = int(input())
    data.append(temp)
    sum += temp

print(sum/x) # print(sum(data) / x)
data.sort()
print(data[(x-1)//2]) # (x-1)//2] middle index
