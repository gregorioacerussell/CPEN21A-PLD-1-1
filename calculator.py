from tkinter import *
win = Tk()

win.geometry("341x517+300+300")
win.title("Calculator")


threelines = Button(win, text="≡", font=("Segoeu UI",15), relief=FLAT)
threelines.place(x=10, y=7)
mode = Label(win, text="Scientific", fg="Brown", font=("Segoe UI", 15))
mode.place(x=45, y=7)
number0 = Label(win, text="0", fg="Black", font=("Segoe UI", 40))
number0.place(x=300, y=30)
DEG = Button(win, text="DEG", font=("Segoeu UI",12), relief=FLAT)
DEG.place(x=10, y=110)
FE = Button(win, text="F-E", font=("Segoeu UI",12), relief=FLAT)
FE.place(x=70, y=110)
MC = Button(win, text="MC", fg="Gray",font=("Segoeu UI",12), relief=FLAT)
MC.place(x=13, y=150)
MR = Button(win, text="MR", fg="Gray",font=("Segoeu UI",12), relief=FLAT)
MR.place(x=70, y=150)
Mplus = Button(win, text="M+", font=("Segoeu UI",12), relief=FLAT)
Mplus.place(x=127, y=150)
Mminus = Button(win, text="M-", font=("Segoeu UI",12), relief=FLAT)
Mminus.place(x=184, y=150)
MS = Button(win, text="MS", font=("Segoeu UI",12), relief=FLAT)
MS.place(x=241, y=150)
Mdown = Button(win, text="M⌄", font=("Segoeu UI",12), relief=FLAT)
Mdown.place(x=298, y=150)
Second = Button(win, text="2nd", bg="Beige",font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
Second.place(x=1, y=190)
Pi = Button(win, text="π", bg="Beige", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
Pi.place(x=70, y=190)
e = Button(win, text="e", bg="Beige", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
e.place(x=138, y=190)
C = Button(win, text="C",  bg="Beige",font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
C.place(x=204, y=190)
Delete = Button(win, text="DEL", bg="Beige",font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
Delete.place(x=274, y=190)
xsquared = Button(win, text="x^2", bg="Beige",font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
xsquared.place(x=1, y=235)
onehalfx = Button(win, text="1/x", bg="Beige",font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
onehalfx.place(x=69, y=235)
absval = Button(win, text="|x|",  bg="Beige",font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
absval.place(x=138, y=235)
exp = Button(win, text="exp",  bg="Beige",font=("Segoeu UI", 10), relief=RAISED,height=2, width=7)
exp.place(x=204, y=235)
mod = Button(win, text="mod",  bg="Beige",font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
mod.place(x=274, y=235)
squarerootofx = Button(win,  bg="Beige",text="√x", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
squarerootofx.place(x=1, y=280)
openparenthesis = Button(win,  bg="Beige",text="(", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
openparenthesis.place(x=70, y=280)
closeparenthesis = Button(win,  bg="Beige",text=")", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
closeparenthesis.place(x=137, y=280)
nexclamation = Button(win,  bg="Beige",text="n!", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
nexclamation.place(x=205, y=280)
division = Button(win,  bg="Beige",text="÷", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
division.place(x=274, y=280)
xraisetoy = Button(win,  bg="Beige",text="x^y", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
xraisetoy.place(x=1, y=326)
seven = Button(win,  bg="Beige",text="7", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
seven.place(x=70, y=326)
eight = Button(win,  bg="Beige",text="8", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
eight.place(x=138, y=326)
nine = Button(win,  bg="Beige",text="9", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
nine.place(x=206, y=326)
x = Button(win,  bg="Beige",text="x", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
x.place(x=274, y=326)
tenraisetox = Button(win,  bg="Beige",text="10^x", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
tenraisetox.place(x=2, y=373)
four = Button(win,  bg="Beige",text="4", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
four.place(x=70, y=373)
five = Button(win,  bg="Beige",text="5", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
five.place(x=138, y=373)
six = Button(win,  bg="Beige",text="6", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
six.place(x=206, y=373)
minus = Button(win,  bg="Beige",text="-", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
minus.place(x=274, y=373)
log = Button(win,  bg="Beige",text="log", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
log.place(x=3, y=420)
one = Button(win,  bg="Beige",text="1", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
one.place(x=70, y=420)
two = Button(win,  bg="Beige",text="2", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
two.place(x=138, y=420)
three = Button(win,  bg="Beige",text="3", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
three.place(x=206, y=420)
plus = Button(win,  bg="Beige",text="+", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
plus.place(x=274, y=420)
ln = Button(win,  bg="Beige",text="ln", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
ln.place(x=3, y=468)
plusminus = Button(win,  bg="Beige",text="+/-", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
plusminus.place(x=71, y=468)
zero = Button(win,  bg="Beige", text="0", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
zero.place(x=138, y=468)
period = Button(win,  bg="Beige", text=".", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
period.place(x=207, y=468)
equals = Button(win,  bg="Beige", text="=", font=("Segoeu UI", 10), relief=RAISED, height=2, width=7)
equals.place(x=274, y=468)
win.mainloop()