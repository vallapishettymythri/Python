#WAP to check two vectors are collinear or not.
x1=int(input("x1:"))
x2=int(input("x2:"))
y1=int(input("y1:"))
y2=int(input("y2:"))
d=(x1*(y2-1))-(x2*(y1-1))+(1*(y1-y2))
if d==0:
    print("Vectors are collinear")
else:
    print("Vectors are not collinear")

#Vector is nothing but which shows direction of a point in the 2d space using its magnitude. 
#to check whether 2 vecors are same or not, we will do determinant if the result of determinant is 0. 
# Then its said vectors are collinear.
