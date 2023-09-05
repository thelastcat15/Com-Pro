x = int(input())

if x > 0 :
    temp = input()
    data = {
        temp : 1
    }
    focus = temp

for _ in range(x-1) :
    temp = input()
    if temp in data :
        data[temp] += 1
    else :
        data[temp] = 1

    if data[focus] < data[temp] :
        focus = temp
    elif data[focus] == data[temp] :
        if int(focus) < int(temp) :
            focus = temp

print("ตอบเลข",focus)