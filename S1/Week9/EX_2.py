x = int(input())

data = []
for _ in range(x) :
    data.append(int(input()))

data.sort()
print(data)
data.sort(reverse=True)
print(data)


#  ข้อนี้โจทย์ผิดต้อง น้อยไปมาก กับ มากไปน้อย สลับที่กัน