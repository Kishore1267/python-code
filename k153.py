from tkinter import *
class matrix:
    def __init__(self,window):
        self.window=window
        self.window.title("welcome to Power MATRIX")
        self.window.geometry('600x400')
        self.window.config(bg='powderblue')
    #Label design
        self.l1=Label(window,text="Enter Base:",font=("Arial Bold",10))
        self.l1.grid(column=0,row=1)
        self.l2=Label(window,text="Enter Exponent:",font=("Arial Bold",10))
        self.l2.grid(column=0,row=10)
    #Text box design
        self.t1=Entry(window,width=20)
        self.t1.grid(column=30,row=1)

        self.t2=Entry(window,width=20)
        self.t2.grid(column=30,row=10)

        self.t3=Entry(window,width=20)
        self.t3.grid(column=30,row=20)



    #Button design
        self.b1=Button(window,text="power",bg="Orange",fg="red",command=self.power)
        self.b1.grid(column=10,row=50)
    #------------function Creation-----------
    def power(self):
        b=int(self.t1.get())
        e=int(self.t2.get())
        po=1
        for i in range(1,e+1):
            po=po*b
        self.t3.delete(0,'end')
        self.t3.insert(0,po)
window=Tk()
obj=matrix(window)
window.mainloop()
