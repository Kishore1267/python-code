# Grade in tkinter
from tkinter import *
w1=Tk()
w1.geometry('600x400')
# -------function for creation----------
def find():
    per=int(t1.get())
    if per<=40:
        result.configure(text='Grade = E')
    elif per<=60:
        result.configure(text='Grade = D')
    elif per<=70:
        result.configure(text='Grade = C')
    elif per<=80:
        result.configure(text='Grade = B')
    else:
        result.configure(text='Grade = A')
def clear():
    t1.delete(0,'end')
    result.configure(text='Result:')
# Label for design
l1 = Label(w1, text="Enter Percentage:", font=("Arial Bold", 10))
t1 = Entry(w1, width=12)

l1.grid(column=0, row=0)

b1 = Button(w1, text="Find", bg="Orange", fg="red", command=find)
b2 = Button(w1, text="clear", bg="Orange", fg="red", command=clear)

result=Message(w1,text="Result:",width=300)
# Text box design
t1.grid(column=20, row=0)

# Button design
b1.grid(column=20, row=3)
b2.grid(column=20, row=4)

result.grid(column=0,row=6,columnspan=2)

window=mainloop()
