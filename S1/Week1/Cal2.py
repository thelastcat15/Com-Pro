while (True) :
    x = input("Enter Number : ")
    if (x=="end") :
        break
    else :
        x = float(x)
    y = int(input("Enter Multiply : "))
    
    n = 1
    temp = x
    while (True) :
        temp = temp*y
        print("Round : %d [%f เศษ %f]"%(n, temp, temp - temp//1))
        if (temp%1 == 0) :
            break
        if (temp > 0) :
            temp -= temp//1
        n += 1
