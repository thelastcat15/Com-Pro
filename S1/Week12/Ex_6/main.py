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

    data_list = list(reader(data))
    for row in data_list :
        txt = " ".join(row)
        print(txt)
        
        writer_csv.writerow(row)
        f_txt.write(txt+"\n")

    data.close()
    f_txt.close()
    f_csv.close()
except :
    print("Error")
