from tkinter import *
w1=Tk()
w1.geometry('600x400')
# -------function for creation----------
def factorial():
    n=int(t1.get())
    f=1
    for i in range(1,n+1):
        f=f*i
    result.configure(text='Factorial number as :')
    t2.insert(0,f)
# Label for design
l1 = Label(w1, text="Enter number : ", font=("Arial Bold", 10))
l1.grid(column=0, row=0)
# Text box design
t1 = Entry(w1, width=12)
t2 = Entry(w1, width=12)
# Button design
b1 = Button(w1, text="Factorial", bg="Orange", fg="red", command=factorial)

# Label for design
l2 = Label(w1, text="Factorial : ", font=("Arial Bold", 10))
l2.grid(column=0, row=1)


result=Message(w1,text="Result:",width=300)
# Text box design
t1.grid(column=20, row=0)
t2.grid(column=20, row=1)

# Button design
b1.grid(column=20, row=3)

result.grid(column=0,row=6,columnspan=2)

window=mainloop()
