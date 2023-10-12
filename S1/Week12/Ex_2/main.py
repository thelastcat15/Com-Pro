# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *

try :
    with open("b.txt",'a',encoding='utf-8') as f:
        f.write("15")

    with open("b.csv",'a',encoding='utf-8') as f:
        f.write("15")
except :
    print("File not found")
