def compute_area(w,l,h):
    return 2*(w*l+h*l+h*w)
h=-float(input("Enter the heigth of the prism:"))
w=float(input("Enter the width of the prism:"))
l=float(input("Enter the length of the prism:"))
print("Area of the prism is:",compute_area(w,l,h))
