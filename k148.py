# Leap year program
from tkinter import *
w1=Tk()
w1.title("MATRIX Leap year program")
#window.geometry('200X300')

# ------------function creation-----------
def find():
    y=int(t1.get())
    if y%2==0:
        result.configure(text='Result: Leap year')
    else:
        result.configure(text='Result: Not Leap year')

# ------------function creation-----------
def clear():
    t1.delete(0,'end')
    result.configure(text='Result:')
# Label design
l1 = Label(w1, text="Enter year:", font=("Arial Bold", 10))
t1 = Entry(w1, width=20)

b1=Button(w1,text='Find',bg="Orange",fg="red",command=find)
b2=Button(w1,text='Clear',bg="Yellow",fg="black",command=clear)
result=Message(w1,text="Result:",width=300)

l1.grid(column=0,row=0)
t1.grid(column=50,row=0)

b1.grid(column=0,row=1)
b2.grid(column=1,row=1)
result.grid(column=0,row=2,columnspan=2)
w1.mainloop()
