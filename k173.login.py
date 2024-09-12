import os
from tkinter import*
import tkinter.messagebox
class login:
    def __init__(self,window):
        self.window=window
        self.window.title("Welcome to STUDENT MANAGEMENT SYSTEM")
        self.window.geometry("600x500+25+25")
        self.window.config(bg='powderblue')
#-------frame yellow color-------
        fees_frame=Frame(self.window,bg='palegoldenrod')
        fees_frame.place(x=50,y=50,height=500,width=500)

#-------Label in frame-----------
        self.l1=Label(fees_frame,text='STUDENT FEES DETAIL',font=('arial',20,'bold'),fg="red",bg="grey")
        self.l1.place(x=90,y=30)

#-------Label in frame for student id no.-----------
        self.l2=Label(fees_frame,text='Enter Student ID no.',font=('arial',12,'bold'),fg="black",bg="lightblue")
        self.l2.place(x=90,y=75)

#--------Entry Box to enter student id no.-------
        self.user=Entry(fees_frame,font=('Times new roman',12,'bold'),fg="green",bg="orange")
        self.user.place(x=250,y=75,width=160,height=25)

#-------Label in frame for book code-----------
        self.l3=Label(fees_frame,text='Enter Book code',font=('arial',12,'bold'),fg="blue",bg="yellow")
        self.l3.place(x=90,y=109)

# -------Label in frame for book name-----------
        self.l4=Label(fees_frame,text='Enter Book name',font=('arial',12,'bold'),fg="black",bg="green")
        self.l4.place(x=90,y=155)

# -------Label in frame for issue date-----------
        self.l5=Label(fees_frame,text='Enter issue date',font=('arial',12,'bold'),fg="brown",bg="lightblue")
        self.l5.place(x=90,y=200)

# -------Label in frame for return date-----------
        self.l6=Label(fees_frame,text='Enter return date',font=('arial',12,'bold'),fg="blue",bg="lightblue")
        self.l6.place(x=90,y=245)

#-------Enter Box to enter user password-----------
        self.sid=Entry(fees_frame,font=('Times new roman',12,'bold'),fg="black",bg="lightblue")
        self.sid.place(x=250,y=110,width=160,height=25)

        self.bcode=Entry(fees_frame,font=('Times new roman',12,'bold'),fg="black",bg="lightblue")
        self.bcode.place(x=250,y=155,width=160,height=25)

        self.bname=Entry(fees_frame,font=('Times new roman',12,'bold'),fg="black",bg="lightblue")
        self.bname.place(x=250,y=200,width=160,height=25)

        self.isdate=Entry(fees_frame,font=('Times new roman',12,'bold'),fg="black",bg="lightblue")
        self.isdate.place(x=250,y=245,width=160,height=25)

        self.retdate=Entry(fees_frame,font=('Times new roman',12,'bold'),fg="black",bg="lightblue")
        self.retdate.place(x=250,y=290,width=160,height=25)




#-------Buttons----------
        self.btnsubmit=Button(fees_frame,text='submit',width=10,font=('aerial',17,'bold'),command=self.submit,bg='Lightblue',relief='raised',borderwidth=3)
        self.btnsubmit.place(x=100,y=330,width=100,height=25)

        self.btnedit=Button(fees_frame,text='edit',width=10,font=('aerial',17,'bold'),command=self.edit,bg='Lightgreen',relief='raised',borderwidth=3)
        self.btnedit.place(x=205,y=330,width=100,height=25)

        self.btndisplay=Button(fees_frame,text='display',width=10,font=('aerial',17,'bold'),command=self.display,bg='red',relief='raised',borderwidth=3)
        self.btndisplay.place(x=310,y=330,width=100,height=25)
#------------------def for reset button------------------------
    def submit(self):
        u=(self.username.get())
        p=(self.password.get())
        if (u==str('matrix')and p==int(123)):
            filename='menu.py'
            os.system(filename)
            os.system('notepad'+filename)
        else:
            tkinter.messagebox.askyesno("login","Error:wrong password")
        self.username.set("")
        self.password.set("")
        #self.text_username.focus()
#---------------------def for reset button-----------------------
    def edit(self):
        self.username.set("")
        self.password.set("")
        # self.text_username.focus()
#------------------code for exit button-------------------
    def display(self):
        self.exit=tkinter.messagebox.askokcancel("Login system","confirm if you want to exit")
        if self.exit>0:
            self.window.destroy()
            return
window=Tk()
obj=login(window)
window.mainloop()
