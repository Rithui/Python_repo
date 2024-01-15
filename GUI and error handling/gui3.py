from tkinter import*
root=Tk()
def info():
    Label(root,text='Hello Python\n').pack()
Button(root,text='GO',command=info).pack()

root.mainloop()
    
