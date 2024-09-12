from tkinter import *
window=Tk()
window.title('welcome to MATRIX')
#window.geometry("200X300")
# ------------function for addition-----------
def total():
    a = float(t1.get())
    b = float(t2.get())
    c = float(t3.get())
    tot = a + b + c
    t4.insert(0, " ")
    t4.insert(0, tot)


# ------------function for subtraction-----------
def average():
    a = float(t1.get())
    b = float(t2.get())
    c = float(t3.get())
    avg = (a + b + c) / 3
    t5.insert(0, " ")
    t5.insert(0, avg)


# Label design
l1 = Label(window, text="Enter a:", font=("Arial Bold", 10))
l1.grid(column=0, row=0)

l2 = Label(window, text="Enter b:", font=("Arial Bold", 10))
l2.grid(column=0, row=10)

l3 = Label(window, text="Enter c:", font=("Arial Bold", 10))
l3.grid(column=0, row=20)

l4 = Label(window, text="Total:", font=("Arial Bold", 10))
l4.grid(column=0, row=30)

l5 = Label(window, text="Average:", font=("Arial Bold", 10))
l5.grid(column=0, row=40)

# Text box design
t1 = Entry(window, width=20)
t1.grid(column=50, row=0)

t2 = Entry(window, width=20)
t2.grid(column=50, row=10)

t3 = Entry(window, width=20)
t3.grid(column=50, row=20)

t4 = Entry(window, width=20)
t4.grid(column=50, row=30)

t5 = Entry(window, width=20)
t5.grid(column=50, row=40)

# Button design
b1 = Button(window, text="Total", bg="Orange", fg="red", command=total)
b1.grid(column=10, row=80)

b2 = Button(window, text="Average", bg="Yellow", fg="Black", command=average)
b2.grid(column=60, row=80)

window.mainloop()
