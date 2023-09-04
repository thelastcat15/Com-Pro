import math

while (True) :
    x = input("Enter Number : ")
    if (x=="end") :
        break
    y = int(input("Enter ^ : "))

    n = 1
    temp = x

    l = len(x.split(".")[0]) - 1
    x = x.replace(".","")

    sum = 0
    for i in x :
        try :
            i = int(i)
        except :
            i = ord(i) - 55
        k =  i * math.pow(y, l)
        sum += k
        print("Round : %d [%d * %d^%d  =  %f]"%(n, i, y, l, k))
        l -= 1
        n += 1
    
    print("\nResult : %f \n"%(sum))

