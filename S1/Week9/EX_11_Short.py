data = sorted([int(input()) for _ in range(int(input()))], reverse=True)
print("ตอบเลข",max(data, key=data.count))

# อย่าไปเขียนแบบนี้ในพวกงานโปรเจคใหญ่ๆนะ เวลากลับมาแก้จะแก้โค้ดยาก
