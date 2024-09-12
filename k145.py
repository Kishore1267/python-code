from tkinter import *
window=Tk()
window.title("welcome to MATRIX")
#window.geometry('600X400')
#------------function for addition-----------
def add():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    t3.insert(0," ")
    t3.insert(0,c)
# ------------function for subtraction-----------
def sub():
    a=int(t1.get())
    b=int(t2.get())
    c=a-b
    t3.insert(0," ")
    t3.insert(0,c)
# -------------function for multipication-------------
def multiply():
    a=int(t1.get())
    b=int(t2.get())
    c=a*b
    t3.insert(0,c)
# ---------------function for division---------------
def division():
    a=int(t1.get())
    b=int(t2.get())
    c=a/b
    t3.insert(0,c)
def percentage():
    a=int(t1.get())
    b=int(t2.get())
    c=a*100/b
    t3.insert(0,c)
# Label design
l1=Label(window,text="Enter a:",font=("Arial Bold",10))
l1.grid(column=0,row=1)
l2=Label(window,text="Enter b:",font=("Arial Bold",10))
l2.grid(column=0,row=10)
l3=Label(window,text="Result:",font=("Arial Bold",10))
l3.grid(column=0,row=20)

# Text box design
t1=Entry(window,width=20)
t1.grid(column=40,row=1)

t2=Entry(window,width=20)
t2.grid(column=40,row=10)

t3=Entry(window,width=20)
t3.grid(column=40,row=20)

# Button design
b1=Button(window,text="Add",bg="Orange",fg="red",command=add)
b1.grid(column=0,row=50)

b2=Button(window,text="Sub",bg="Yellow",fg="Black",command=sub)
b2.grid(column=30,row=50)

b3=Button(window,text="Multiply",bg="Orange",fg="red",command=multiply)
b3.grid(column=150,row=50)

b4=Button(window,text="division",bg="Yellow",fg="Black",command=division)
b4.grid(column=300,row=50)

b5=Button(window,text="percentage",bg="Green",fg="red",command=percentage)
b5.grid(column=450,row=50)


window.mainloop()
