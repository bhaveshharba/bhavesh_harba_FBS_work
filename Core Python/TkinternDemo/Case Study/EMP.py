from tkinter import *
from tkinter import messagebox

def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()
 

def empManage():
    clearScreen()

    def addEmp():
        pass
    
    def selEmp():
        pass

    def updEmp():
        pass

    def delEmp():
        pass


    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)

    id_label = Label(frame1, text='ID :')
    id_entry = Entry(frame1)
    nm_label = Label(frame1, text='Name :')
    nm_entry = Entry(frame1)
    sal_label = Label(frame1, text='Salary :')
    sal_entry = Entry(frame1)

    id_label.grid(row=1, column=1)
    id_entry.grid(row=1, column=2)
    nm_label.grid(row=2, column=1)
    nm_entry.grid(row=2, column=2)
    sal_label.grid(row=3, column=1)
    sal_entry.grid(row=3, column=2)
    frame1.pack()


    add_btn = Button(frame2, text='ADD', command=addEmp)
    sel_btn = Button(frame2, text='SELECT', command=selEmp)
    upd_btn = Button(frame2, text='UPDATE', command=updEmp)
    del_btn = Button(frame2, text='SELECT', command=delEmp)

    add_btn.pack(side=LEFT)
    sel_btn.pack(side=LEFT)
    upd_btn.pack(side=LEFT)
    del_btn.pack(side=LEFT)
    frame2.pack()

    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(frame3, yscrollcommand=scrollbar.set, height=15, width=40)
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    frame3.pack()

def login():
    uid = uid_entry.get()
    pas = pas_entry.get()

    if(uid == 'Admin' and pas == '1234'):
        empManage()
    else:
        messagebox.showerror('Error', message='Invalid Credentials...')


def main():
    uid_label = Label(window, text='User ID :', pady=10)
    global uid_entry
    uid_entry = Entry(window)
    pas_label = Label(window, text='Password', pady=10)
    global pas_entry
    pas_entry = Entry(window)
    btn = Button(window, text='Login', command=login,)

    uid_label.pack()
    uid_entry.pack()
    pas_label.pack()
    pas_entry.pack()
    btn.pack()


if (__name__ == '__main__'):
    window = Tk()
    window.geometry('300x500')


    # main()
    empManage()

    window.mainloop()
