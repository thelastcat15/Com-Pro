x = int(input())


for num in range(2,x+1) : # 2 - x
  for i in range(2,num+1) : # 2 - i
    if num == i :
      print(num) # เป็นจำนวนเฉพาะ
    if num % i == 0 :
      break # ไม่ใช่จำนวนเฉพาะ
