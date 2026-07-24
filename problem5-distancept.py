#we need to find the distance of a point in two dimension. 
# where we require x1,x2,y1,y2
x1=int(input("Enter x1:"))
x2=int(input("Enter x2:"))
y1=int(input("Enter y1"))
y2=int(input("Enter y2"))
distance=(((y2-y1)**2)+((x2-x1)**2)**0.5)
print("Distance:", distance)
