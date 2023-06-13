from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=54, borderwidth=9)
e.grid(row=0, column=0, columnspan=3, padx=12, pady=11)


def calc(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def calc_clear():
    e.delete(0, END)


def calc_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def calc_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtract":
        e.insert(0, f_num - int(second_number))
    
    if math == "multiply":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

def calc_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def calc_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def calc_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)

# define  buttons
b1 = Button(root, text="7", padx=40, pady=20, command= lambda: calc(7), borderwidth=7)
b2 = Button(root, text="8", padx=40, pady=20, command= lambda: calc(8), borderwidth=7)
b3 = Button(root, text="9", padx=40, pady=20, command= lambda: calc(9), borderwidth=7)
b4 = Button(root, text="4", padx=40, pady=20, command= lambda: calc(4), borderwidth=7)
b5 = Button(root, text="5", padx=40, pady=20, command= lambda: calc(5), borderwidth=7)
b6 = Button(root, text="6", padx=40, pady=20, command= lambda: calc(6), borderwidth=7)
b7 = Button(root, text="1", padx=40, pady=20, command= lambda: calc(1), borderwidth=7)
b8 = Button(root, text="2", padx=40, pady=20, command= lambda: calc(2), borderwidth=7)
b9 = Button(root, text="3", padx=40, pady=20, command= lambda: calc(3), borderwidth=7)
b0 = Button(root, text="0", padx=40, pady=20, command= lambda: calc(0), borderwidth=7)
b_multiply = Button(root, text="*", padx=40, pady=20, command= calc_multiply, borderwidth=7)
b_division = Button(root, text="/", padx=40, pady=20, command= calc_division, borderwidth=7)
b_subtract = Button(root, text="-", padx=40, pady=20, command= calc_subtract, borderwidth=7)

b_add = Button(root, text="+", padx=39, pady=20, command= calc_add, borderwidth=7)
b_equal = Button(root, text="=", padx=39, pady=20, command= calc_equal, borderwidth=7)
b_clear = Button(root, text="C", padx=39, pady=20, command= calc_clear, borderwidth=7)


#buttons on the screen
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
b_add.grid(row=4, column=1)
b_equal.grid(row=5, column=0)
b_clear.grid(row=4, column=2)

b_multiply.grid(row=5, column=1)
b_division.grid(row=5, column=2)
b_subtract.grid(row=6, column=0)

root.mainloop()
