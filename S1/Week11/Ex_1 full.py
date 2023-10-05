from tkinter import *

f = Tk()
f.geometry("260x250")
f.resizable(False,False)

def cal():
    new_data = [Temp_Var1, Temp_Var2, Temp_Var3, Temp_Var4, Temp_Var5]
    avg = sum(new_data)/5
    _min = int(min(new_data))
    _max = int(max(new_data))

    Result_Var.set((avg,"/",_max,"/",_min))

# ========================================================================================

Temp_Var1 = DoubleVar()
Temp_Var1.set()
Label(f, text="คะแนนนักศึกษาคนที่ 1").place(x=10,y=10)
Entry(f, textvariable=Temp_Var1).place(x=120,y=10)

Temp_Var2 = DoubleVar()
Temp_Var2.set()
Label(f, text="คะแนนนักศึกษาคนที่ 2").place(x=10,y=31)
Entry(f, textvariable=Temp_Var2).place(x=120,y=31)

Temp_Var3 = DoubleVar()
Temp_Var3.set()
Label(f, text="คะแนนนักศึกษาคนที่ 3").place(x=10,y=52)
Entry(f, textvariable=Temp_Var3).place(x=120,y=52)

Temp_Var4 = DoubleVar()
Temp_Var4.set()
Label(f, text="คะแนนนักศึกษาคนที่ 4").place(x=10,y=73)
Entry(f, textvariable=Temp_Var4).place(x=120,y=73)

Temp_Var5 = DoubleVar()
Temp_Var5.set()
Label(f, text="คะแนนนักศึกษาคนที่ 5").place(x=10,y=94)
Entry(f, textvariable=Temp_Var5).place(x=120,y=94)

# ========================================================================================

Label(f, text="คะแนนเฉลี่ย / คะแนนมากสุด / คะแนนน้อยสุด").place(relx=0.5,y=125,anchor=CENTER)
Result_Var = StringVar()
Result_Var.set("")
Label(f, textvariable=Result_Var).place(relx=0.5,y=146,anchor=CENTER)
Button(f, width=10, text="Calculate", command=cal).place(x=5,y=200)


f.mainloop()