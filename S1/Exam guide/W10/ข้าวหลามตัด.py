x = int(input())

def create(center) :
    list_line = [i for i in range(1,center)] + [i for i in range(center,0,-1)] # สร้างเป็น list
    return " | ".join(map(str, list_line)) # connect


for i in range(1,x) :
    print("    "*(x-i) + create(i))

for i in range(x,0,-1) :
    print("    "*(x-i) + create(i))