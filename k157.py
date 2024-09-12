
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#root window
window=tk.Tk()
window.geometry('300x220')
window.resizable(False,False)
window.title('MATRIX COMPUTERS Radio button Demo')

def show_result():
    showinfo(title='Result',message=selected_size.get())
selected_size=tk.StringVar()
sizes=(('ADD','1')),(('SUB','2')),(('MULTIPLY','3')),(('DIVIDE','4')),(('PERCENTAGE','5'))

#Label
l1=ttk.Label(text="Enter your choice")
l1.pack(fill='x',padx=5,pady=5)

#radio button
for i in sizes:
    r=ttk.Radiobutton(window,text=i[0],value=i[1],variable=selected_size)
    r.pack(fill='x',padx=5,pady=5)

#button
button=ttk.Button(window,text="Get Selected Option",command=show_result)
button.pack(fill='x',padx=5,pady=5)
window.mainloop()





