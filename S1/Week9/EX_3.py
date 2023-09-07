x = int(input())

data = []
for _ in range(x) :
    temp = int(input())
    data.append(temp)

print(sum(data)/x) # print(sum(data) / x)
data.sort()
print(data[(x-1)//2]) # (x-1)//2] middle index
