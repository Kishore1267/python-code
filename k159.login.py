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
        login_frame=Frame(self.window,bg='palegoldenrod')
        login_frame.place(x=50,y=50,height=350,width=500)
#-------Label in frame-----------
        self.l1=Label(login_frame,text='STUDENT LOGIN FORM',font=('arial',20,'bold'),fg="red",bg="grey")
        self.l1.place(x=90,y=30)
#-------Label in frame for username-----------
        self.l2=Label(login_frame,text='Enter User Name',font=('arial',12,'bold'),fg="black",bg="lightblue")
        self.l2.place(x=90,y=75)
#--------Entry Box to enter user name-------
        self.user=Entry(login_frame,font=('Times new roman',12,'bold'),fg="green",bg="lightblue")
        self.user.place(x=250,y=75,width=160,height=25)
#-------Label in frame for password-----------
        self.l3=Label(login_frame,text='Enter password',font=('arial',12,'bold'),fg="blue",bg="lightblue")
        self.l3.place(x=90,y=110)
#-------Enter Box to enter user password-----------
        self.pas=Entry(login_frame,font=('Times new roman',12,'bold'),fg="black",bg="lightblue")
        self.pas.place(x=250,y=110,width=160,height=25)
#-------Buttons----------
        self.btnlogin=Button(login_frame,text='Login',width=10,font=('aerial',17,'bold'),command=self.Login,bg='Lightblue',relief='raised',borderwidth=3)
        self.btnlogin.place(x=90,y=150,width=100,height=25)

        self.btnreset=Button(login_frame,text='Login',width=10,font=('aerial',17,'bold'),command=self.Reset,bg='Lightgreen',relief='raised',borderwidth=3)
        self.btnreset.place(x=200,y=150,width=100,height=25)

        self.btnexit=Button(login_frame,text='Exit',width=10,font=('aerial',17,'bold'),command=self.Exit,bg='red',relief='raised',borderwidth=3)
        self.btnexit.place(x=310,y=150,width=100,height=25)

#------------------coding for login-------------------
    def Login(self):
        u=(self.username.get())
        p=(self.password.get())
        if(u==str('matrix')and p==int(123)):
            filename='menu.py'
            os.system(filename)
            os.system('notepad'+filename)
        else:
         tkinter.messagebox.askyesno("login","Error:Wrong password")
         self.username.set("")
         self.password.set("")
         #self.text_username.focus()
#------------------def for reset button------------------------
    def Reset(self):
        self.username.set("")
        self.password.set("")
        #self.text_username.focus()
#------------------code for exit button-------------------
    def Exit(self):
        self.exit=tkinter.messagebox.askokcancel("Login system","confirm if you want to exit")
        if self.exit>0:
            self.window.destroy()
            return
window=Tk()
obj=login(window)
window.mainloop()








