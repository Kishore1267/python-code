# G3 in tkinter
from tkinter import *
w1=Tk()
w1.geometry('600x400')
# -------function for creation----------
def find():
    a=int(t1.get())
    b=int(t2.get())
    c=int(t3.get())
    if a==b and a==c:
        result.configure(text='Result: All are equal')
    elif a>b and a>c:
        result.configure(text='Result: A is greatest')
    elif b>c:
        result.configure(text='Result: B is greatest')
    else:
        result.configure(text='Result: C is greatest')
def clear():
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')
    result.configure(text='Result:')
# Label for design
l1 = Label(w1, text="Enter A:", font=("Arial Bold", 10))
l2 = Label(w1, text="Enter B:", font=("Arial Bold", 10))
l3 = Label(w1, text="Enter C:", font=("Arial Bold", 10))

t1 = Entry(w1, width=12)
t2 = Entry(w1, width=12)
t3 = Entry(w1, width=12)

l1.grid(column=0, row=0)
l2.grid(column=0, row=1)
l3.grid(column=0, row=2)

b1 = Button(w1, text="Find", bg="Orange", fg="red", command=find)
b2 = Button(w1, text="clear", bg="Orange", fg="red", command=clear)

result=Message(w1,text="Result:",width=300)
# Text box design
t1.grid(column=20, row=0)
t2.grid(column=20, row=1)
t3.grid(column=20, row=2)

# Button design
b1.grid(column=20, row=3)
b2.grid(column=20, row=4)

result.grid(column=0,row=6,columnspan=2)

window=mainloop()
