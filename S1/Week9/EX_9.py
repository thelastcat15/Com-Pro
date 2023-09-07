x = int(input())

data = []
for _ in range(x) :
    data.append(int(input()))

data.sort()

max = data[x-1]
min = data[0]

print(max)
print(min)

# ห้ามใช้ฟังก์ชัน max() min()
# ข้อนี้ Grader จารย์ล็อคให้ใช้ฟังก์ชัน sort นั่งงมกับ for loop ตั้งนาน555
