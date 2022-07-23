from tkinter import *

root = Tk()
root.title("Clone Calculator")


e = Entry(root, width=50, borderwidth=3)
e.grid(row=0, column=0, columnspan=4)

#Get the number from each buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#Clear function
def button_clear():
    e.delete(0, END)

#addition Function
def button_add():
    fnum = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(fnum)
    e.delete(0, END)

#addition Function
def button_sub():
    fnum = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(fnum)
    e.delete(0, END)

#addition Function
def button_multi():
    fnum = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(fnum)
    e.delete(0, END)

#addition Function
def button_div():
    fnum = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(fnum)
    e.delete(0, END)

#Equal Function
def button_equals():
    secondNum = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(secondNum))
    if math == "subtraction":
        e.insert(0, f_num - int(secondNum))
    if math == "multiply":
        e.insert(0, f_num * int(secondNum))
    if math == "division":
        e.insert(0, f_num / int(secondNum))

myButton1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
myButton2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
myButton3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
myButton4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
myButton5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
myButton6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
myButton7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
myButton8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
myButton9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
myButton0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
myButton_blank1 = Button(root, text=" ", padx=42, pady=20)
myButton_blank2 = Button(root, text=" ", padx=41, pady=20)

myButton_add = Button(root, text="+", padx=38, pady=20, command=button_add)
myButton_sub = Button(root, text="-", padx=40, pady=20, command=button_sub)
myButton_div = Button(root, text="/", padx=40, pady=20, command=button_div)
myButton_multi = Button(root, text="*", padx=40, pady=20, command=button_multi)
myButton_equals = Button(root, text="=", padx=87, pady=20, command=button_equals)
myButton_clear = Button(root, text="CLEAR", padx=73, pady=20, command=button_clear)


#row4
myButton_blank1.grid(row=4, column=0)
myButton0.grid(row=4, column=1)
myButton_blank2.grid(row=4, column=2)
myButton_add.grid(row=4, column=3)

#row3
myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)
myButton_sub.grid(row=3, column=3)

#row2
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton_div.grid(row=2, column=3)

#row1
myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)
myButton9.grid(row=1, column=2)
myButton_multi.grid(row=1, column=3)

#row 5
myButton_equals.grid(row=5, column=0, columnspan=2)
myButton_clear.grid(row=5, column=2, columnspan=2)






root = mainloop()