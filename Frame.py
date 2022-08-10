from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def buttonpush():
    messagebox.showinfo(title='msg', message='HAHA, that is GOOD')
    

top = Tk()
top.title("test")
top.geometry('500x500') 

Button_1 = Button(top, text='Button 1', command=buttonpush)
Button_2 = Button(top, text='Button 2')
spbox_1 = ttk.Spinbox(
    top, 
    text='spbox 1', 
    from_=0, 
    to=20,
    width=5
    )

Button_1.pack()
Button_2.pack()
spbox_1.pack()


top.mainloop()