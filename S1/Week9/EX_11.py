x = int(input())

data = []
for _ in range(x) :
    data.append(int(input()))
data.sort(reverse=True)

focus_number = data[0]
focus_value = 0

for i in set(data) :
    temp = data.count(i)
    if temp > focus_number :
        focus_number = i
        focus_value = temp
    elif temp == focus_number :
        if i > focus_number :
            focus_number = i
            focus_value = temp

print("ตอบเลข",focus_number)