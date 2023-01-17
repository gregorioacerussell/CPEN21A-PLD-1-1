from tkinter import *
win = Tk()

# widget gui
win.geometry("600x400+300+300")
win.title("My First GUI Application")


# label widget
title = Label(win, text="My First GUI", fg="Black", font=("Verdana", 15))
title.place(x=253, y=80)

lbl = Label(win, text="Label 1:", fg="Black", font=("Times New Roman", 12))
lbl.place(x=170, y= 125)

lbl2 = Label(win, text="Label 2:", fg="Black", font=("Times New Roman", 12))
lbl2.place(x=170, y=160)

# entry widget
txtbox = Entry(win, width=30, bd=4, relief=GROOVE)
txtbox.place(x=240, y=130)

txtbox2 = Entry(win, width=30, bd=4, relief=GROOVE)
txtbox2.place(x=240, y=163)

# button widgets
btn = Button(win, text="Yes", fg="Blue", font=("Arial", 11))
btn.place(x=240, y=200)

btn2 = Button(win, text="No", fg="Red", font=("Arial", 11))
btn2.place(x=310, y=200)


# radiobutton widget
def sel():
    selection = f"You selected option {var.get()}"
    label.config(text=selection)
var = IntVar()
r1 = Radiobutton(win, text="Male", variable=var,value=1, command=sel)
r1.place(x=230, y=240)

r2 = Radiobutton(win, text="Female", variable=var,value=2, command=sel)
r2.place(x=305, y=240)

label = Label(win)
label.place(x=230, y=270)
win.mainloop()