data = {} # ถ้าไม่เก็บ name ใช้ List

while True :
    name, point = input().split(" ")
    if name == "-1" or point == "-1" :
        break
    
    data[name] = int(point)


print(sum(data.values()) / len(data))