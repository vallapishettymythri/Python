#WAP where p lies in a certain radius of the circle
r=int(input("Radius:"))
x=int(input("x:"))
y=int(input("y:"))
distance=((x**2)+(y**2))**0.5
if distance<r:
    print("Point inside")
if distance > r:
    print("Point outside the circle")
if distance==r:
    print("Point lies on the circle")