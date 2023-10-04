from tkinter import *

f = Tk()
f.geometry("260x250")
f.resizable(False,False)

def cal():
    new_data = [item.get() for item in data]
    avg = sum(new_data)/5
    _min = int(min(new_data))
    _max = int(max(new_data))

    Result_Var.set((avg,"/",_max,"/",_min))

data = []
dis_y = 0
for i in range(5):
    Temp_Var = DoubleVar()
    Temp_Var.set("")
    Label(f, text="คะแนนนักศึกษาคนที่ "+str(i+1)).place(x=10,y=10+dis_y)
    Entry(f, textvariable=Temp_Var, ).place(x=120,y=10+dis_y)
    dis_y += 21
    data.append(Temp_Var)


Label(f, text="คะแนนเฉลี่ย / คะแนนมากสุด / คะแนนน้อยสุด").place(relx=0.5,y=125,anchor=CENTER)
Result_Var = StringVar()
Result_Var.set("")
Label(f, textvariable=Result_Var).place(relx=0.5,y=146,anchor=CENTER)
Button(f, text="Calculate", command=cal).place(relx=0.5,y=229,anchor=CENTER)


f.mainloop()