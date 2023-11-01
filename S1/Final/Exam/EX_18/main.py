# index   0      1      2      3      4      5      6
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

a = eval(input("a: "))      # autoแปลงเป็น float หรือ int
b = eval(input("b: "))      # autoแปลงเป็น float หรือ int

n = a + b
dn = n % 7      # หารเก็บเศษ เช่น 15 % 7 = 1

print(days[dn]) # days[index] เช่น days[3] ก็จะได้ 'Wed'