x = int(input())

def create(center) :
    list_line = [i for i in range(1,center)] + [i for i in range(center,0,-1)] # สร้างเป็น list
    return "    "*(x-center) + " | ".join(map(str, list_line))


for i in range(1,x) :
    print(create(i))

for i in range(x,0,-1) :
    print(create(i))