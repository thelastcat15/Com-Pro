while (True) :
    x = input("Enter Number : ")
    if (x=="end") :
        break
    else :
        x = int(x)
    y = int(input("Enter Divide : "))

    n = 1
    temp = x
    while (True) :
        h = temp%y
        temp = temp/y
        print("Round : %d [%d เศษ %d]"%(n, temp, h))
        n += 1
        if (y > temp) :
            break