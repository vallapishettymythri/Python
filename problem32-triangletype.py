#Triangle Type Determination
#Write a Python code to check whether a triangle is Equilateral, Isosceles or Scalene.
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or c==a:
    print("Isosceles triangle")
else:
    print("Scalene triangle")