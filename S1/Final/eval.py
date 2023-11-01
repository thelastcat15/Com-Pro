"""
eval(expression, globals, locals)

ในข้อสอบ eval ไม่น่าจะใช้ globals กับ locals

expression อาจจะเป็นสูตรหรือนิพจน์ทางคณิตศาสตร์หรือการคำนวณที่เขียนเป็นข้อความที่สามารถให้ผลลัพธ์ตามที่มีในโปรแกรม Python
!! expression ต้องเป็น str เท่านั้น !!
"""

x = eval("5")               # เหมือนกับ x = 5
print(x)                    # 5
print(type(x))              # <class 'int'>

y = eval("0.5")             # โปรแกรมคำนวณ 0.5 แต่ไม่แสดงผล เหมือนกับ y = 0.5
print(y)                    # 0.5
print(type(y))              # <class 'float'>

z = eval("2 + 3")           # โปรแกรมคำนวณ 2 + 3 แต่ไม่แสดงผล เหมือนกับ y = 2 + 3
print(z)                    # 5

# eval ใช้รันโค้ด 1 บรรทัดได้ด้วยนะ
z = eval("print('hi')")     # hi
print(type(z))              # <class 'NoneType'>


eval("print(z)")            # 5  (z จากบรรทัดที่ 15)

"""
ตัวอย่างการประยุกต์ใช้

x = input()         # ไม่รู้ว่าต้องใช้ int() หรือ float()
x = eval(input())   # ทีนี้มันก็จะแปลงให้เลย
"""