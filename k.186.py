from tkinter import *
w1=Tk()
w1.geometry('600x400')
# -------function for creation----------
def perfect():
    n=int(t1.get())
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
    result.configure(text='sum')
    if sum==2*n:
        result.configure(text='perfect number ')
    else:
        result.configure(text=' Not perfect number ')
    t2.insert(0,sum)
# Label for design
l1 = Label(w1, text=" Enter number : ", font=("Arial Bold", 10))
l1.grid(column=0, row=0)
# Text box design
t1 = Entry(w1, width=12)
t2 = Entry(w1, width=12)
# Button design
b1 = Button(w1, text="perfect", bg="Orange", fg="red", command=perfect)
# Label for design
l2 = Label(w1, text="sum", font=("Arial Bold", 10))
l2.grid(column=0, row=1)


result=Message(w1,text="Result:",width=300)
# Text box design
t1.grid(column=20, row=0)
t2.grid(column=20, row=1)

# Button design
b1.grid(column=20, row=3)

result.grid(column=0,row=6,columnspan=2)

window=mainloop()
