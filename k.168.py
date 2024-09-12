# Area of triangle in tkinter
from tkinter import *
window=Tk()
window.title('welcome to MATRIX')
# -------function for creation----------
def find():
    b=float(t1.get())
    h=float(t2.get())
    ar=1/2*b*h
    t3.insert(0," ")
    t3.insert(0,ar)
# Label for design
l1 = Label(window, text="Enter base:", font=("Arial Bold", 10))
l1.grid(column=0, row=0)

l2 = Label(window, text="Enter height:", font=("Arial Bold", 10))
l2.grid(column=0, row=10)

l3 = Label(window, text="Area:", font=("Arial Bold", 10))
l3.grid(column=0, row=20)

# Text box design
t1 = Entry(window, width=20)
t1.grid(column=50, row=0)

t2 = Entry(window, width=20)
t2.grid(column=50, row=10)

t3 = Entry(window, width=20)
t3.grid(column=50, row=20)

# Button design
b1 = Button(window, text="find", bg="Orange", fg="red", command=find)
b1.grid(column=10, row=80)

window=mainloop()
