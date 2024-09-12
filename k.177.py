# Swapping in tkinter
from tkinter import *
window=Tk()
window.title('welcome to MATRIX')
# -------function for creation----------
def swap():
    a=int(t1.get())
    b=int(t2.get())
    c=a
    a=b
    b=c
    t3.insert(0,a)
    t4.insert(0,b)
# Label for design
l1 = Label(window, text="Enter a:", font=("Arial Bold", 10))
l1.grid(column=0, row=0)

l2 = Label(window, text="Enter b:", font=("Arial Bold", 10))
l2.grid(column=0, row=10)

# Text box design
t1 = Entry(window, width=20)
t1.grid(column=50, row=0)

t2 = Entry(window, width=20)
t2.grid(column=50, row=10)

# Button design
b1 = Button(window, text="swap", bg="Orange", fg="red", command=swap)
b1.grid(column=10, row=80)

# Label for design

l3 = Label(window, text="After swapping a = ", font=("Arial Bold", 10))
l3.grid(column=0, row=20)

l4 = Label(window, text="After swapping b = ", font=("Arial Bold", 10))
l4.grid(column=0, row=30)

# Text box design
t3 = Entry(window, width=20)
t3.grid(column=50, row=20)

t4 = Entry(window, width=20)
t4.grid(column=50, row=30)

window=mainloop()
