def centi(F):
    C=(F-32)*5/9
    return C

F=input("Enter the temprature in fareinheit:")
F=float(F)
print("The temprature in centigrade is:",centi(F))
