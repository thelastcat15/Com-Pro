from tkinter import *

f = Tk()
f.geometry("260x250")
f.resizable(False,False)

def check():
    input_value = Selec_Var.get()
    if input_value == 1:
        Result_Var.set("ถูกต้องคับผม")
    else :
        Result_Var.set("ผิดนะคับ ลองใหม่ๆ")


Label(f, text="ผมชอบสีอะไร ?").place(x=10,y=10)

Selec_Var = IntVar()
Radiobutton(f, text="สีฟ้า", variable=Selec_Var, value=1).place(x=110,y=22)
Radiobutton(f, text="สีแดง", variable=Selec_Var, value=2).place(x=110,y=47)
Radiobutton(f, text="สีดำ", variable=Selec_Var, value=3).place(x=110,y=72)
Radiobutton(f, text="สีเขียว", variable=Selec_Var, value=4).place(x=110,y=47)

Result_Var = StringVar()
Result_Var.set("")
Label(f, textvariable=Result_Var).place(x=110,y=140)
Button(f, width=10, text="Check", command=check).place(x=5,y=200)


f.mainloop()








