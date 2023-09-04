money = 5000.50

mode = int(input())

if (mode == 1 or mode == 2) :
    x = float(input())

    if (mode == 1) : money += x
    else : money -= x

print(round(money, 2))