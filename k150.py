from tkinter import *
w1=Tk()
w1.title("MATRIX Power program")
w1.geometry('600x400')

# ------------function creation-----------
def Power():
    b=int(t1.get())
    e=int(t2.get())
    po=1
    for i in range(1,e+1):
        po=po*b
    t3.delete(0,"end")
    t3.insert(0, po)

# Label design
l1 = Label(w1, text="Enter Base    :", font=("Arial Bold", 10))
l2 = Label(w1, text="Enter Exponent:", font=("Arial Bold", 10))
l3 = Label(w1, text="Power         :", font=("Arial Bold", 10))

t1 = Entry(w1, width=20)
t2 = Entry(w1, width=20)
t3 = Entry(w1, width=20)

b1=Button(w1,text='Find',bg="Orange",fg="red",command=Power)

l1.grid(column=1,row=1)
l2.grid(column=1,row=10)
l3.grid(column=1,row=20)

t1.grid(column=40,row=1)
t2.grid(column=40,row=10)
t3.grid(column=40,row=20)

b1.grid(column=30,row=30)

w1.mainloop()
