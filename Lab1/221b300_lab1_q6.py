def avg(a,b,c,d,e,f):
    avg=sum(a,b,c,d,e,f)/6
    return avg
    

a,b,c,d,e,f=input("Enter the grade obtained foe the 6 numbers:").split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
print("The average of the marks are:",avg(a,b,c,d,e,f))
