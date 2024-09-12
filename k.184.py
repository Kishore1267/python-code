from tkinter import *
w1=Tk()
w1.geometry('600x400')
# -------function for creation----------
def power():
    b=int(t1.get())
    e=int(t2.get())
    po=1
    for i in range(1,e+1):
        po=po*b
    result.configure(text='power as :')
    t3.insert(0,po)
# Label for design
l1 = Label(w1, text="Enter base : ", font=("Arial Bold", 10))
l1.grid(column=0, row=0)

l2 = Label(w1, text="Enter exponent: ", font=("Arial Bold", 10))
l2.grid(column=0, row=1)

l3 = Label(w1, text="power: ", font=("Arial Bold", 10))
l3.grid(column=0, row=2)


# Text box design
t1 = Entry(w1, width=12)
t2 = Entry(w1, width=12)
t3 = Entry(w1, width=12)

# Button design
b1 = Button(w1, text="power", bg="Orange", fg="red", command=power)
result=Message(w1,text="Result:",width=300)
# Text box design
t1.grid(column=20, row=0)
t2.grid(column=20, row=1)
t3.grid(column=20, row=2)

# Button design
b1.grid(column=20, row=3)

result.grid(column=0,row=6,columnspan=2)

window=mainloop()
