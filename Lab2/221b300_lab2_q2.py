#this is the code for findig the area of the given triangle
def area(b,h):
    area=0.5*b*h
    return area

b=int(input("Enter the base length:"))
h=int(input("nter the altitude:"))
print("Area of the given triangle is:",area(b,h))
