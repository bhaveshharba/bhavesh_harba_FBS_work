from tkinter import *
from tkinter import messagebox

def submit():
    val1 = x.get()
    val2 = y.get()
    val3 = z.get()
    # print(val1)

    data =''
    if(val1 == 1):
        data += 'Python\n'
    if(val2 == 1):
        data += 'Java\n'
    if(val3 == 1):
        data += 'Testing\n'
        
    if(data):
        messagebox.showinfo('Cource', message=data)
    else:
        messagebox.showwarning('Warning', message='Please select cource....')

    

if(__name__ == '__main__'):
    Window = Tk()
    Window.geometry('300x500')
    Window.config(background='gray')

    x = IntVar()
    y = IntVar()
    z = IntVar()

    frame1 = Frame(Window)
    frame2 = Frame(Window)
    frame3 = Frame(Window)

    label1 = Label(frame1, text='Please select cource',)

    label1.pack()
    frame1.pack()

    chk1 = Checkbutton(frame2, text='Python', variable=x)
    chk2 = Checkbutton(frame2, text='Java', variable=y)
    chk3 = Checkbutton(frame2, text='Testing', variable=z)

    chk1.pack(side=LEFT)
    chk2.pack(side=LEFT)
    chk3.pack(side=LEFT)
    frame2.pack()

    btn = Button(frame3, text='Submit', command=submit)
    btn.pack()
    frame3.pack()
    
 
    Window.mainloop()