from tkinter import*
root=Tk()
root.geometry('1920x1200')
root.configure(bg='yellow')
Label(root,text='second Screen',font='Arial 30 bold',bg='yellow',fy='yellow')
def fun(e=0):
    root.destroy()
    import demo_first_window
Button(root,text='Prev',command=fun).pack()
root.mainloop()
