from tkinter import *
w1=Tk()
w1.title("MATRIX Factorial program")
w1.geometry('600x400')
# ------------function creation-----------
def factorial():
    n=int(t1.get())
    f=1
    for i in range(1,n+1):
        f=f*i
    result.configure(text='Result:')
def clear():
    t1.delete(0," ")
    result.configure(text='Result:')
# Label design
l1 = Label(w1, text="Enter number:", font=("Arial Bold", 10))
t1 = Entry(w1, width=20)
l2 = Label(w1, text="Factorial number:", font=("Arial Bold", 10))
t2 = Entry(w1, width=20)


b1=Button(w1,text='Factorial',bg="Orange",fg="red",command=factorial)
b2=Button(w1,text='Clear',bg="Yellow",fg="black",command=clear)
result=Message(w1,text="Result:",width=300)

l1.grid(column=0,row=0)
t1.grid(column=50,row=0)

l1.grid(column=0,row=10)
t1.grid(column=50,row=0)

b1.grid(column=0,row=1)
b2.grid(column=50,row=10)
result.grid(column=0,row=2,columnspan=2)
w1.mainloop()
