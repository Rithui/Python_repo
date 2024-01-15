def avg(a,b,c):
    A=a+b+c/3
    return A

a,b,c=input("Enter the numbers:").split()
a=float(a)
b=float(b)
c=float(c)
print("The average of the numbers is:",avg(a,b,c))
