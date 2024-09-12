import tkinter as tk
from tkinter import*

class matrix:
    def __init__(self,window):
        self.window=tk.Tk()
        self.window.title("Registration form for STUDENT")
        self.window.geometry('900x900')
        self.window.resizable(False,False)
        self.window.config(bg='powderblue')
        #Label design
        self.l1=Label(self.window,text="Student registration form :",font=("Arial Bold",10))
        self.l1.grid(column=30,row=10)

        self.l2=Label(self.window,text="Enter name:",font=("Arial Bold",10))
        self.l2.grid(column=30,row=30)

        self.l3=Label(self.window,text="Enter age:",font=("Arial Bold",10))
        self.l3.grid(column=30,row=50)

        self.l4=Label(self.window,text="Roll number:",font=("Arial Bold",10))
        self.l4.grid(column=30,row=70)

        self.l5=Label(self.window,text="Enter address:",font=("Arial Bold",10))
        self.l5.grid(column=30,row=90)

        self.l6=Label(self.window,text="Enter mobile number:",font=("Arial Bold",10))
        self.l6.grid(column=30,row=110)

        self.l7=Label(self.window,text="Gender:",font=("Arial Bold",10))
        self.l7.grid(column=30,row=130)

        self.l8=Label(self.window,text="Enter Branch:",font=("Arial Bold",10))
        self.l8.grid(column=30,row=150)

        self.l9=Label(self.window,text="Enter Subject:",font=("Arial Bold",10))
        self.l9.grid(column=30,row=170)

    #Text box design
        self.t1=Entry(self.window,width=20)
        self.t1.grid(column=50,row=30)

        self.t2=Entry(self.window,width=20)
        self.t2.grid(column=50,row=30)

        self.t3=Entry(self.window,width=20)
        self.t3.grid(column=50,row=50)

        self.t4=Entry(self.window,width=20)
        self.t4.grid(column=50,row=70)

        self.t5=Entry(self.window,width=20)
        self.t5.grid(column=50,row=90)

        self.t6=Entry(self.window,width=20)
        self.t6.grid(column=50,row=110)

        self.t7=Entry(self.window,width=20)
        self.t7.grid(column=50,row=130)

        self.t8=Entry(self.window,width=20)
        self.t8.grid(column=50,row=150)

        self.t9=Entry(self.window,width=20)
        self.t9.grid(column=50,row=170)


    #Button design
        self.b1=Button(self.window,text="submit",bg="Orange",fg="red")
        self.b1.grid(column=30,row=190)

window=Tk()
obj=matrix(window)
window.mainloop()
