
lines=input("Ener the first statement:")
words=input("Ener the second statement:")
count=0
w1=lines.split()
w2=words.split()
for w in w1:
    for k in w2:
        if(w==k):
            count=count+1


if(count!=0):
    print("Present")

else:
    print("Not present")
