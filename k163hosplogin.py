import tkinter as tk
from tkinter import *

class matrix:
    def __init__(self,window):
        self.window=tk.Tk()
        self.window.title("Welcome to HOSPITAL MANAGEMENT SYSTEM")
        self.window.geometry('900x900')
        self.window.resizable(False,False)
        self.window.config(bg='powderblue')
        #Label design
        self.l1=Label(self.window,text="HOSPITAL MANAGEMENT SYSTEM",font=("Arial Bold",10))
        self.l1.grid(column=30,row=10)

        self.l2=Label(self.window,text="Name of tablets:",font=("Arial Bold",10))
        self.l2.grid(column=30,row=30)

        self.l3=Label(self.window,text="Reference number:",font=("Arial Bold",10))
        self.l3.grid(column=30,row=50)

        self.l4=Label(self.window,text="Dose:",font=("Arial Bold",10))
        self.l4.grid(column=30,row=70)

        self.l5=Label(self.window,text="No. of tablets:",font=("Arial Bold",10))
        self.l5.grid(column=30,row=90)

        self.l6=Label(self.window,text="Lots:",font=("Arial Bold",10))
        self.l6.grid(column=30,row=110)

        self.l7=Label(self.window,text="Issue date:",font=("Arial Bold",10))
        self.l7.grid(column=30,row=130)

        self.l8=Label(self.window,text="Exp date:",font=("Arial Bold",10))
        self.l8.grid(column=30,row=150)

        self.l9=Label(self.window,text="Daily dose:",font=("Arial Bold",10))
        self.l9.grid(column=30,row=170)

        self.l10=Label(self.window,text="Side effect:",font=("Arial Bold",10))
        self.l10.grid(column=30,row=190)

        self.l11=Label(self.window,text="Further information:",font=("Arial Bold",10))
        self.l11.grid(column=30,row=210)

        self.l12=Label(self.window,text="Blood Pressure:",font=("Arial Bold",10))
        self.l12.grid(column=30,row=230)

        self.l13=Label(self.window,text="Storage Advice:",font=("Arial Bold",10))
        self.l13.grid(column=30,row=250)

        self.l14=Label(self.window,text="Medication:",font=("Arial Bold",10))
        self.l14.grid(column=30,row=270)

        self.l15=Label(self.window,text="Patient id:",font=("Arial Bold",10))
        self.l15.grid(column=30,row=290)

        self.l16=Label(self.window,text="NHS number:",font=("Arial Bold",10))
        self.l16.grid(column=30,row=310)

        self.l17=Label(self.window,text="Patient name:",font=("Arial Bold",10))
        self.l17.grid(column=30,row=330)

        self.l18=Label(self.window,text="Date of Birth:",font=("Arial Bold",10))
        self.l18.grid(column=30,row=350)

        self.l19=Label(self.window,text="Patient address:",font=("Arial Bold",10))
        self.l19.grid(column=30,row=370)


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

        self.t10=Entry(self.window,width=20)
        self.t10.grid(column=50,row=190)

        self.t11=Entry(self.window,width=20)
        self.t11.grid(column=50,row=210)

        self.t12=Entry(self.window,width=20)
        self.t12.grid(column=50,row=230)

        self.t13=Entry(self.window,width=20)
        self.t13.grid(column=50,row=250)

        self.t14=Entry(self.window,width=20)
        self.t14.grid(column=50,row=270)

        self.t15=Entry(self.window,width=20)
        self.t15.grid(column=50,row=290)

        self.t16=Entry(self.window,width=20)
        self.t16.grid(column=50,row=310)

        self.t17=Entry(self.window,width=20)
        self.t17.grid(column=50,row=330)

        self.t18=Entry(self.window,width=20)
        self.t18.grid(column=50,row=350)

        self.t19=Entry(self.window,width=20)
        self.t19.grid(column=50,row=370)
    #Button design
        self.b1=Button(self.window,text="Prescription",bg="Orange",fg="red")
        self.b1.grid(column=30,row=390)

        self.b2=Button(self.window,text="Prescription date",bg="white",fg="red")
        self.b2.grid(column=30,row=410)

        self.b3=Button(self.window,text="Update",bg="green",fg="red")
        self.b3.grid(column=30,row=430)

        self.b4=Button(self.window,text="Delete",bg="light blue",fg="red")
        self.b4.grid(column=30,row=450)

        self.b5=Button(self.window,text="clear",bg="yellow",fg="red")
        self.b5.grid(column=30,row=470)

        self.b6=Button(self.window,text="Exit",bg="grey",fg="red")
        self.b6.grid(column=30,row=490)

window=Tk()
obj=matrix(window)
window.mainloop()
