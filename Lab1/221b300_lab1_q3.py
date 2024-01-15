def simple(P,r,t):
    A=P*(1+r*t)
    return A

def compound(P,r,t):
    B=P*pow((1+r/100),t)
    return B
    

P=input("Enter the principle amount:")
r=input("Enter the rate of intrest:")
t=input("Enter the duration of years:")
P=int(P)
r=float(r)
t=int(t)
print("The simple intrest of the principle amount is:",simple(P,r,t))
print("The compound intrest of the principle amount is:",compound(P,r,t))
