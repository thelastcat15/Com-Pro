def allsum():
    b=number[0]+number[1]+number[2]+number[3]+number[4]
    return b

number=[]
for i in range(5):
    a=int(input())
    number.append(a)

print(allsum())
