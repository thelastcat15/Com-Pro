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

    sum = 0
    for row in list(reader(data)) :
        print(row[0], "ได้", row[1], "คะแนน")
        sum += int(row[1])

        writer_csv.writerow(row)
        f_txt.write(",".join(row)+"\n")
    print("คะแนนรวม", sum)

    data.close()
    f_txt.close()
    f_csv.close()
except :
    print("Error")
