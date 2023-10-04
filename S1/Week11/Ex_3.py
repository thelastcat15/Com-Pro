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

choices = {
    "สีฟ้า" : 1,
    "สีแดง" : 2,
    "สีดำ" : 3,
    "สีเขียว" : 4
}

Label(f, text="ผมชอบสีอะไร ?").place(x=10,y=10)

dis_y = 0
Selec_Var = IntVar()
for quest, val in choices.items():
    Radiobutton(f, text=quest, variable=Selec_Var,value=val).place(x=110,y=22+dis_y)
    dis_y += 25

Result_Var = StringVar()
Result_Var.set("")
Label(f, textvariable=Result_Var).place(x=110,y=140)
Button(f, width=10, text="Check", command=check).place(x=5,y=200)


f.mainloop()