

#this is the code for swapping the given numbers    
n=int(input("Enter the first input numebr:"))
m=int(input("Enter the second input number:"))
if m>0 and n>0:
         m=m+n
         n=m-n
         m=m-n

print("The swapped version of the given variables are:",m,n)
