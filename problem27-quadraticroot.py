#Quadratic Equation Roots
#Write a Python code to calculate the root of a quadratic equation.
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=(b**2)-4*a*c
if d>0:
    print("Two distinct real roots")
elif d==0:
    print("One repeated real root")
else:
    print("Roots are imaginary; No solution.")
