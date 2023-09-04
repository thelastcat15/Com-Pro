from numpy import array, median

x = int(input())

data = []
for _ in range(x) :
    data.append(int(input()))
num_data = array(data)

print(num_data.mean())
print(median(num_data))