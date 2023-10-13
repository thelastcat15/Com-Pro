# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *



try :
    with open("c.csv", "r") as f:
        r = reader(f)
        l = list(r)
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i][1]
    print(sum)
except :
    print("Error")