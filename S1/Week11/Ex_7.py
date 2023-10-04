from tkinter import *

f = Tk()
f.geometry("150x110")
f.resizable(False,False)

grades = "FFFFFDCBAAA"
def cal():
    current_value = recive.get()
    if current_value < 0 :
        display.set("E")
    else :
        display.set(grades[current_value//10])

recive = IntVar()
recive.set("")
Entry(f, textvariable=recive).pack()

recive2 = IntVar()
recive2.set("")
Entry(f, textvariable=recive2).pack()

display = StringVar()
display.set("")
Label(f, textvariable=display).pack()

Button(f, text="-", command=lambda: display.set(recive.get() - recive2.get())).place(relx=0.2, y=90, anchor=W)
Button(f, text="+", command=lambda: display.set(recive.get() + recive2.get())).place(relx=0.5, y=90, anchor=CENTER)
Button(f, text="*", command=lambda: display.set(recive.get() * recive2.get())).place(relx=0.8, y=90, anchor=E)

f.mainloop()