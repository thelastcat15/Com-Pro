# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *



try :
    data = input()
    with open("b.txt",'w',encoding='utf-8') as f_txt :
        f_txt.write(data)

    with open("b.csv",'w',encoding='utf-8') as f_csv :
        w = writer(f_csv, lineterminator="\n")
        w.writerow([data])
except :
    print("Error")

