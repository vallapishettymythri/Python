# Geometrical Shapes Area Calculator
#Write a Python code which computes the area of various geometrical shapes
#using a menu-driven approach.
print("1.circle")
print("2.Rectangle")
print("3.sqaure")
print("4.triangle")
choose=int(input("From 1-4"))
if choose==1:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of Circle =", area)

elif choose==2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    print("Area of Rectangle =", area)
elif choose==3:
    s = float(input("Enter side: "))
    area = s * s
    print("Area of Square =", area)
    
elif choose==4:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print("Area of Triangle =", area)
else:
    print("Invalid")
