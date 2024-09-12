from tkinter import *
class matrix:
    def __init__(self,window):
        self.window=window
        self.window.title("welcome to Reverse number MATRIX")
        self.window.geometry('600x400')
        self.window.config(bg='powderblue')
    #Label design
        self.l1=Label(window,text="Enter number:",font=("Arial Bold",10))
        self.l1.grid(column=0,row=1)
        self.l2=Label(window,text="Reverse number:",font=("Arial Bold",10))
        self.l2.grid(column=0,row=10)
    #Text box design
        self.t1=Entry(window,width=20)
        self.t1.grid(column=30,row=1)

        self.t2=Entry(window,width=20)
        self.t2.grid(column=30,row=10)

    #Button design
        self.b1=Button(window,text="reverse",bg="Orange",fg="red",command=self.reverse)
        self.b1.grid(column=10,row=50)
    #------------function Creation-----------
    def reverse(self):
        n=int(self.t1.get())
        rev=0
        while(n>0):
            mod=n%10
            rev=rev*10+mod
            n=n//10
        self.t2.delete(0,'end')
        self.t2.insert(0,rev)

window=Tk()
obj=matrix(window)
window.mainloop()
