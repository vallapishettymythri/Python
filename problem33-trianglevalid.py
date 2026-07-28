#Triangle Validity by Angles
#Write a Python code to check whether a triangle can be formed with the given
#values for the angles.
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a+b+c==180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")
