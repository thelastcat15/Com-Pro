# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *



try :
    a = input()
    f = open("b.txt", "w", encoding="utf-8")
    f.write(str(a))
    f.close()

    with open("b.csv", "w", encoding="utf-8") as f:
        w = writer(f, lineterminator="\n")
        w.writerow([a])
except :
    print("Error")