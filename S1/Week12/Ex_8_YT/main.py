# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *



try :
    with open("a.csv", "r") as f:
        r = reader(f)
        l = list(r)
        s = 0
        for i in range(len(l)) :
            s = s + int(l[i][0])
        avg = s/len(l)
    with open("b.csv", "w", encoding="utf-8") as f:
        w = writer(f, lineterminator="\n")
        w.writerow([avg])
except :
    print("Error")
