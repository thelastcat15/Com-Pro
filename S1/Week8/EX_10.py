x = int(input())

for i in range(x) :
    for ii in range(i) :
        print("  ",end="")

    for ii in range(x-i) :
        ii = ii + 1
        print("" + str(ii) + "|", end="")
    
    print("")

