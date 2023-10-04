from tkinter import *

f = Tk()
f.geometry("260x250")
f.resizable(False,False)


def cal():
    input_value = Input_Var.get()
    if input_value <= 10:
        price = input_value * 5
    elif input_value <= 30:
        price = 50 + (input_value - 10) * 4.5
    else:
        price = 140 + (input_value - 30) * 4
    Result_Var.set(price)


Input_Var = DoubleVar()
Input_Var.set("")
Label(f, text="ค่าไฟฟ้า").place(x=10,y=10)
Entry(f, textvariable=Input_Var).place(x=120,y=10)

Result_Var = DoubleVar()
Result_Var.set("")
Label(f, text="ค่าใช้จ่าย").place(x=10,y=31)
Label(f, textvariable=Result_Var).place(x=120,y=31)
Button(f, width=10, text="Calculate", command=cal).place(x=5,y=200)

f.mainloop()