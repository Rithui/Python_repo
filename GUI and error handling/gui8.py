from tkinter import*
root=Tk()
root.title("Calculator")
root.geometry("300x300")
Label(root,text="Enter the first number").pack()
var1=Entry(root)
var1.pack()
Label(root,text="Enter the second number").pack()
var2=Entry(root)
var2.pack()
def myevent():
    Label(root,text=int(var1.get())+int(var2.get())).pack()
Button(root,text="show",command=myevent).pack()
root.mainloop()
