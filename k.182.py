# quadratic equation in tkinter
import math
from tkinter import *
w1=Tk()
w1.geometry('600x400')
#window.geometry('600X400')
#------------function for addition-----------
def find():
    a=int(t1.get())
    b=int(t2.get())
    c=int(t3.get())
    d=b*b-4*a*c
    if d>0:
        result.configure(text='Two different roots')
        r1=(-b+math.sqrt(b))/2*a
        result.configure(text='Root 1')
        r2=(-b-math.sqrt(b))/2*a
        result.configure(text='Root 2')
    elif d==0:
        result.configure(text='same roots')
        r1=r2=-b/2*a
        result.configure(text='Root 1')
        result.configure(text='Root 2')
    else:
        result.configure(text='Roots are not possible')
    t1.insert(0,'end')
    t2.insert(0,'end')
    t3.insert(0,'end')
    t4.insert(0,r1)
    t5.insert(0,r2)
    result.configure(text='Result')
# Label design
l1=Label(w1,text="Enter a:",font=("Arial Bold",10))
l1.grid(column=0,row=1)

l2=Label(w1,text="Enter b:",font=("Arial Bold",10))
l2.grid(column=0,row=10)

l3=Label(w1,text="Enter c:",font=("Arial Bold",10))
l3.grid(column=0,row=20)

l4=Label(w1,text="Root 1:",font=("Arial Bold",10))
l4.grid(column=0,row=30)

l5=Label(w1,text="Root 2:",font=("Arial Bold",10))
l5.grid(column=0,row=40)

# Text box design
t1=Entry(w1,width=20)
t1.grid(column=40,row=1)

t2=Entry(w1,width=20)
t2.grid(column=40,row=10)

t3=Entry(w1,width=20)
t3.grid(column=40,row=20)

t4=Entry(w1,width=20)
t4.grid(column=40,row=30)

t5=Entry(w1,width=20)
t5.grid(column=40,row=40)


# Button design
b1=Button(w1,text="find",bg="Orange",fg="red",command=find)
b1.grid(column=0,row=50)

result=Message(w1,text='Result',width=300)

w1.mainloop()
