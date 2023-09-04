a = int(input())
b = int(input())
c = int(input())
d = int(input())

min_ = min(a,b,c,d)
for i in range (min_, 0, -1) :
    if (a % i == 0) and (b % i == 0) and (c % i == 0) and (d % i == 0) :
        print(i)
        break
