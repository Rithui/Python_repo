#this is hte code for finding the groos salary of a person
def GRS(bs):
    da=(10*bs)/100
    ta=(12*bs)/100
    gs=bs+ta+da
    return gs

bs=int(input("nter the base salary:"))
print("The gross salary is:",GRS(bs))
