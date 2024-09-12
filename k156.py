from tkinter import *
class matrix:
    def __init__(self,window):
        self.window=window
        self.window.title("welcome to MATRIX")
        self.window.geometry('900x900')
        self.window.config(bg='powderblue')
    #----------Frame design--------------
        self.f1=Frame(self.window,bg='red',borderwidth=6,width=6,relief=SUNKEN)
        self.f1.pack(side="left",padx=1,pady=1)
        self.l1=Label(self.f1,text="Left frame",font=("Arial Bold",10))
        self.l1.pack(pady=1,padx=1)
        self.b1=Button(self.f1,text="add",bg="Orange",fg="red")
        self.b1.pack()
        self.lw1 = Label(self.window, text="Enter a:", font=("Arial Bold", 10))
        self.lw1.pack()

'''
        f2 = Frame(self.window, bg='blue', borderwidth=6, width=6, relief=SUNKEN)
        f2.pack(side="right",fill="y", padx=1, pady=1)
        self.l2 = Label(f2, text="Right frame", font=("Arial Bold", 10))
        self.l2.pack(pady=1, padx=1)
        self.b2 = Button(self.window, text="sub", bg="purple", fg="red")
        self.b2.pack()
        self.lw2 = Label(self.window, text="Enter b:", font=("Arial Bold", 10))
        self.lw2.pack()

        f3 = Frame(self.window, bg='green', borderwidth=6, width=6, relief=SUNKEN)
        f3.pack(side="top", padx=1, pady=1)
        self.l3 = Label(f3, text="Top frame", font=("Arial Bold", 10))
        self.l3.pack(pady=5, padx=5)
        self.b3 = Button(self.window, text="multiply", bg="grey", fg="red")
        self.b3.pack()
        self.lw3 = Label(self.window, text="Enter c:", font=("Arial Bold", 10))
        self.lw3.pack()

        f4 = Frame(self.window, bg='Yellow', borderwidth=6, width=6, relief=SUNKEN)
        f4.pack(side="bottom",fill="y", padx=10, pady=10)
        self.l4 = Label(f4, text="Bottom frame", font=("Arial Bold", 10))
        self.l4.pack(pady=10,padx=10)
        self.b4 = Button(self.window, text="divide", bg="dark green", fg="red")
        self.b4.pack()
        self.lw4 = Label(self.window, text="Enter d:", font=("Arial Bold", 10))
        self.lw4.pack()
'''


window=Tk()
obj=matrix(window)
window.mainloop()
