from tkinter import*
root=Tk()
root.title("B9 batch")
root.geometry('300x300')
Label(root,text='enter the your fristname').pack()
var1=Entry(root)
var1.pack()
Label(root,text='enter the lastname').pack()
var2=Entry(root)
var2.pack()
def myevent():
    Label(root,text=var1.get()+' '+var2.get()).pack()
Button(root,text='Show',command=myevent).pack()

root.mainloop()
