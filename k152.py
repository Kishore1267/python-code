from tkinter import *
class matrix:
    def __init__(self,window):
        self.window=window
        self.window.title("welcome to MATRIX")
        self.window.geometry('600x400')
        self.window.config(bg='powderblue')
    #Label design
        self.l1=Label(window,text="Enter number:",font=("Arial Bold",10))
        self.l1.grid(column=0,row=1)
        self.l2=Label(window,text="Factorial number:",font=("Arial Bold",10))
        self.l2.grid(column=0,row=10)
    #Text box design
        self.t1=Entry(window,width=20)
        self.t1.grid(column=30,row=1)

        self.t2=Entry(window,width=20)
        self.t2.grid(column=30,row=10)

    #Button design
        self.b1=Button(window,text="Factorial",bg="Orange",fg="red",command=self.factorial)
        self.b1.grid(column=10,row=50)
        self.b2=Button(window,text="clear",bg="Orange",fg="red",command=self.clear)
        self.b2.grid(column=30,row=50)

    #------------function Creation-----------
    def factorial(self):
        n=int(self.t1.get())
        f=1
        for i in range(1,n+1):
            f=f*i
        self.t2.delete(0,'end')
        self.t2.insert(0,f)

    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0,'end')
window=Tk()
obj=matrix(window)
window.mainloop()
