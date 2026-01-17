from tkinter import *
root = Tk()
# root.geometry('300x500')
f = Frame(root, bg='red')
f.pack()
Label(f, text="Inside Frame").pack()
root.mainloop()