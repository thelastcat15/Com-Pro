x = int(input())


for i in range(x+1, 1, -1) :
    for ii in range(i-1) :
        ii += 1
        print(""+str(ii)+"|", end="")
    print()