data = {}

while True :
    name, point = input().split(" ")
    if name == "-1" :
        break
    data[name] = int(point)


print(sum(data.values()) / len(data))