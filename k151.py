from tkinter import *
class matrix:
    def __init__(self,window):
        self.window=window
        self.window.title("welcome to MATRIX")
        self.window.geometry('600x400')
        self.window.config(bg='powderblue')
    #Label design
        self.l1=Label(window,text="Enter a:",font=("Arial Bold",10))
        self.l1.grid(column=0,row=1)
        self.l2=Label(window,text="Enter b:",font=("Arial Bold",10))
        self.l2.grid(column=0,row=10)
        self.l3=Label(window,text="Result:",font=("Arial Bold",10))
        self.l3.grid(column=0,row=20)

    #Text box design
        self.t1=Entry(window,width=20)
        self.t1.grid(column=30,row=1)

        self.t2=Entry(window,width=20)
        self.t2.grid(column=30,row=10)

        self.t3=Entry(window,width=20)
        self.t3.grid(column=30,row=20)

    #Button design
        self.b1=Button(window,text="Add",bg="Orange",fg="red",command=self.add)
        self.b1.grid(column=10,row=50)

        self.b2=Button(window,text="Sub",bg="Yellow",fg="Black",command=self.sub)
        self.b2.grid(column=20,row=50)

        self.b3=Button(window,text="Multiply",bg="Orange",fg="red",command=self.multiply)
        self.b3.grid(column=30,row=50)

        self.b4=Button(window,text="division",bg="Yellow",fg="Black",command=self.division)
        self.b4.grid(column=40,row=50)

        self.b5=Button(window,text="percentage",bg="Yellow",fg="Black",command=self.percentage)
        self.b5.grid(column=50,row=50)

    #------------function for addition-----------
    def add(self):
        a=int(self.t1.get())
        b=int(self.t2.get())
        c=a+b
        self.t3.delete(0,'end')
        self.t3.insert(0,c)
    #------------function for subtraction-----------
    def sub(self):
        a=int(self.t1.get())
        b=int(self.t2.get())
        c=a-b
        self.t3.delete(0,'end')
        self.t3.insert(0,c)
    #-------------function for multipication-------------
    def multiply(self):
        a=int(self.t1.get())
        b=int(self.t2.get())
        c=a*b
        self.t3.delete(0,'end')
        self.t3.insert(0,c)
    #---------------function for division---------------
    def division(self):
        a=int(self.t1.get())
        b=int(self.t2.get())
        c=a/b
        self.t3.delete(0,'end')
        self.t3.insert(0,c)
    #---------------function for percentage--------------
    def percentage(self):
        a = int(self.t1.get())
        b = int(self.t2.get())
        c = (a*100)/b
        self.t3.delete(0,'end')
        self.t3.insert(0, c)
window=Tk()
obj=matrix(window)
window.mainloop()
