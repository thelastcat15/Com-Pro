from tkinter import *

f = Tk()
f.geometry("150x100")
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

display = StringVar()
display.set("")
Label(f, textvariable=display).pack()

Button(f, text="Grade", command=cal).pack()

f.mainloop()