def compute_volume(h,r):
    return 3.14*r*r*h
h=float(input("Enter the height:"))
d=float(input("Enter the diameter:"))
r=d/2
print("Volume if the cylinder",compute_volume(h,r))
