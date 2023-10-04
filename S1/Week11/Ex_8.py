from tkinter import *

f = Tk()
f.geometry("150x80")
f.resizable(False,False)

last_pos = ""

# def add_point(count, pos):
#     if last_pos != pos : count = 0
#     count += 1
#     if Even and pos == "Left":
#         Display_Var.set("O")
#     elif not Even and pos == "Left":
#         Display_Var.set("X")
#     last_pos = pos

count = 0
Display_Var = StringVar()
Display_Var.set("X")
Button(f, textvariable=Display_Var, width=7, height=3, command=lambda: add_point(count, "left")).place(relx=0, rely=0.5, anchor=W)
Button(f, text="+", width=7, height=3, command=lambda: add_point(count, "right")).place(relx=1, rely=0.5, anchor=E)



f.mainloop()