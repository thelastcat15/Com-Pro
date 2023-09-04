x = int(input())


if x == 1 :
    print("No prime number")
else :
    for i in range(2, x+1) :
        if i == x :
            print("prime number")
            break
        else :
            if x % i == 0 :
                print("No prime number")
                break