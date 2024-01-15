def compound_intrest(p,r,t):
    si=p*(1+r)**t-p
    print("compound intrest:",si)


p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate of intres:"))
t=int(input("Enter the time period:"))
compound_intrest(p,r,t)
