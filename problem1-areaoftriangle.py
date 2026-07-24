#formal to find area of triangle by herons is Area=s*(s-a)*(s-b)*s-c)**0.5. 
# Where s will be a+b+c/2
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
s=(a+b+c)/2
Area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is:", Area);
