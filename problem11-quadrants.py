#WAP to check whether point lies in which quadrant
x=int(input("x:"))
y=int(input("y:"))
if x>0 and y>0:
    print("1st quadrant")
if x<0 and y>0:
    print("2nd quadrant")
if x<0 and y<0:
    print("3rd quadrant")
if x>0 and y<0:
    print("4th quadrant")