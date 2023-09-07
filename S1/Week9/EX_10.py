x = int(input())

data = []
for _ in range(x) :
    data.append(int(input()))

print(sorted(data))
print(sorted(data, reverse=True))


# ห้ามใช้ฟังก์ชัน sort() แต่เหมือนจารย์จะไม่ได้ห้ามใช้ sorted()
