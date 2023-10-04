from tkinter import *

f = Tk()
f.geometry("150x100")
f.resizable(False,False)

def cal():
    current_value = recive.get()
    if current_value % 2 :
        display.set("จำนวนคี่")
    else :
        display.set("จำนวนคู่")

recive = IntVar()
Entry(f, textvariable=recive).pack()

display = StringVar()
display.set("0")
Label(f, textvariable=display).pack()

Button(f, text="Grade", command=cal).pack()

f.mainloop()