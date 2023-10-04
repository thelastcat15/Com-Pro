from tkinter import *

f = Tk()
f.geometry("150x100")
f.resizable(False,False)

display = IntVar()
display.set(5)
Label(f, textvariable=display).pack()
Button(f, text="+", command=lambda: display.set(display.get() + 1)).pack()
Button(f, text="-", command=lambda: display.set(display.get() - 1)).pack()

f.mainloop()