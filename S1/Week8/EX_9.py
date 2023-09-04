x = int(input())

for i in range(x) :
    print("  "*(x-i-1), end="")
    for ii in range(i+1) :
        ii += 1
        print(str(ii)+"|", end="")

    print("")