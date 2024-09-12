# Reverse number in tkinter
from tkinter import *
window=Tk()
window.title('welcome to MATRIX')
# -------function for creation----------
def reverse():
    n=int(t1.get())
    u=n%10
    n=n//10
    t=n%10
    h=n//10
    no = h * 1 + t * 10 + u * 100
    t2.insert(0,no)
# Label for design
l1 = Label(window, text="Enter number:", font=("Arial Bold", 10))
l1.grid(column=0, row=0)
# Text box design
t1 = Entry(window, width=20)
t1.grid(column=50, row=0)

# Button design
b1 = Button(window, text="reverse", bg="Orange", fg="red", command=reverse)
b1.grid(column=10, row=80)

# Label for design

l2 = Label(window, text="Reverse", font=("Arial Bold", 10))
l2.grid(column=0, row=20)

# Text box design
t2 = Entry(window, width=20)
t2.grid(column=50, row=20)

window=mainloop()
