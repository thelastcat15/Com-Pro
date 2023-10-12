# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *



try :
    f_txt = open("b.txt",'r',encoding='utf-8')
    f_csv = open("b.csv",'r',encoding='utf-8')

    print(f_txt.read())
    print(list(reader(f_csv)))

    f_txt.close()
    f_csv.close()
except :
    print("Error")
