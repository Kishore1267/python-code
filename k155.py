from tkinter import *
class matrix:
    def __init__(self,window):
        self.window=window
        self.window.title("welcome to Reverse number MATRIX")
        self.window.geometry('600x400')
        self.window.config(bg='powderblue')
    #Label design
        self.l1=Label(window,text="Enter a:",font=("Arial Bold",10))
        self.l1.grid(column=0,row=1)
        self.l2=Label(window,text="Enter b:",font=("Arial Bold",10))
        self.l2.grid(column=0,row=10)
    #Text box design
        self.t1=Entry(window,width=20)
        self.t1.grid(column=30,row=1)

        self.t2=Entry(window,width=20)
        self.t2.grid(column=30,row=10)

        self.result=Message(window,text='Result:',width=300)
        self.result.grid(column=10,row=20,columnspan=2)

    #Button design
        self.b1=Button(window,text="G2",bg="Orange",fg="red",command=self.G2)
        self.b1.grid(column=10,row=50)
    #------------function Creation-----------
    def G2(self):
        a=int(self.t1.get())
        b=int(self.t2.get())
        if a==b:
            self.result.configure(text='Result:Both are equal')
        elif a>b:
            self.result.configure(text='Result:A is greater')
        else:
            self.result.configure(text='Result:B is greater')


window=Tk()
obj=matrix(window)
window.mainloop()
