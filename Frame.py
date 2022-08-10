import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



class GUIFrame():

    def __init__(self):
        self.frame = Tk()
        self.init_window()
        
        self.frame.mainloop()

    def init_window(self):
        # window
        self.frame.title('hehe')
        self.frame.geometry("400x400")
        self.frame.resizable(0, 0)

        # text
        self.titleText = Text(self.frame, text="PointCounter")
        self.titleText.grid(row = 1, column = 1)

        # button
        self.Button_1 = Button(self.frame, text="button 1")
        self.Button_2 = Button(self.frame, text="button 2")

        self.Button_1.grid(row = 0, column = 0)
        self.Button_2.grid(row = 0, column = 1)

    def buttonpush():
        messagebox.showinfo(title='msg', message='HAHA, that is GOOD')

def gui_start():
    sysFrame = GUIFrame()

gui_start()