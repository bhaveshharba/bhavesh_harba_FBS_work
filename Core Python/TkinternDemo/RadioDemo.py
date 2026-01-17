from tkinter import *
from tkinter import messagebox

def ChangeTheme():
    val = x.get()
    print(val)
    if(val == 1):
        window.config(background='black')
    elif(val == 2):
        window.config(background='orange')
    elif(val == 3):
        window.config(background='yellow')
    else:
        messagebox.showwarning('Warning',message='Please select theme')
        

if (__name__ == '__main__'):
    window = Tk()
    window.title('Radio Button Demo')
    window.geometry('300x500')
    window.config(background='grey')

    x = IntVar()

    label = Label(window,text='Please select background color')
    rdo1 = Radiobutton(window, text='Black', variable=x, value=1)
    rdo2 = Radiobutton(window, text='Orange', variable=x, value=2)
    rdo3 = Radiobutton(window, text='Yellow', variable=x, value=3)
    btn = Button(window,text='Change theme',command=ChangeTheme)

    # label.pack()
    # rdo1.pack(side=LEFT)
    # rdo2.pack(side=LEFT)
    # rdo3.pack(side=LEFT)
    # btn.pack(side=LEFT)

    label.grid(row=1,column=1)
    rdo1.grid(row=2,column=1)
    rdo2.grid(row=3,column=1)
    rdo3.grid(row=4,column=1)
    btn.grid(row=5,column=1,columnspan=2)


    window.mainloop()