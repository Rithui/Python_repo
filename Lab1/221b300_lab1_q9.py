#this is the code for finding the greatest of the given numbers
def great(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>c:
        return b
    else:
        return c
    
a,b,c=input("Give the numbers:").split()
a=int(a)
b=int(b)
c=int(c)
print("The greatest of the given numbers is:",great(a,b,c))
