x = int(input()) + 1

def create(center) :
    list_line = list(range(1,center)) + list(range(center,0,-1))
    return "|".join(map(str, list_line)) # connect

for i in range(1,x) :
    print("  "*(x-i) + create(i) + "|")

for i in range(x, 0, -1):
    print("  "*(x-i) + create(i) + "|")
