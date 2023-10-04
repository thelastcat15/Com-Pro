from tkinter import *

f = Tk()
f.geometry("270x250")
f.resizable(False,False)

def check():
    text = ""
    for txt, val in choices.items():
        print()
        if val.get() == 1:
            text += txt+","
    Result_Var.set("ผม"+text[:-1])

choices = {
    "ชอบเล่นเกม" : None,
    "ชอบดูหนัง" : None,
    "ชอบฟังเพลง" : None,
    "ชอบหลับในคาบ" : None
}

dis_y = 0
for txt in choices:
    Selec_Var = IntVar()
    Checkbutton(f, text=txt, variable=Selec_Var).place(x=10,y=22+dis_y)
    choices[txt] = Selec_Var
    dis_y += 25

Result_Var = StringVar()
Result_Var.set("")
Label(f, textvariable=Result_Var).place(x=10,y=140)
Button(f, width=10, text="Check", command=check).place(x=5,y=200)


f.mainloop()