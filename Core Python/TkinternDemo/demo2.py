from tkinter import *

if (__name__ == '__main__'):
    window = Tk()
    window.config(bg='black')
    window.geometry('300x500')
    label = Label(window,text='Hello World',background='red')
    label.pack()


    window.mainloop()
