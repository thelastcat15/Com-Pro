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
    
    data_list = list(
        map(
            lambda temp: int(temp[0]),
            list(reader(data))
        )
    )
    print(data_list)

    avg = str( sum(data_list) / len(data_list) )
    
    writer_csv.writerow([avg])
    f_txt.write(avg)

    data.close()
    f_txt.close()
    f_csv.close()
except :
    print("Error")
