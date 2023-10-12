# ===================== Change Path =============================
import os
os.chdir(os.path.dirname(__file__))
# ===================== Change Path =============================
from csv import *



try :
    data = open("data.csv",'r',encoding='utf-8')
    f_txt = open("b.txt",'w',encoding='utf-8')
    f_csv = open("b.csv",'w',encoding='utf-8')

    writer_csv = writer(f_csv, lineterminator="\n")

    for row in list(reader(data)) :
        writer_csv.writerow(row)
        f_txt.write(",".join(row)+"\n")

    data.close()
    f_txt.close()
    f_csv.close()
except :
    print("File not found")
