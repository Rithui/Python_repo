from tkinter import*
root=Tk()
root.geometry('1920x1200')
root.configure(bg='light green')
Label(root,text='First Screen',font='Arial 30 bold',bg='ligth green',fy='green')
def fun(e=0):
    root.destroy()
    import demo_second_window
Button(root,text='Next',command=fun).pack()
root.mainloop()
