from tkinter import *


# IntVar()
# StringVar()
# DoubleVar()
# BooleanVar()

f = Tk()
f.geometry("260x250")
f.resizable(False,False)

txt = StringVar()
txt.set("สวัสดี")
Label(f, textvariable=txt).place(x=0,y=0,anchor=CENTER)


f.mainloop()