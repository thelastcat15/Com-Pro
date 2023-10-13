# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *



try :
    with open("b.csv", "r", encoding="utf-8") as f:
        r = reader(f)
        l = list(r)
        print(l)
    f = open("b.txt", "r", encoding="utf-8")
    a = f.read()
    print(a)
    f.close()
except :
    print("Error")