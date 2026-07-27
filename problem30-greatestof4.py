#wap to find the greatest among 4 numbers
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
if a>b and a>c and a>d:
    print("a is greater")
elif b>a and b>c and b>d:
    print("b is greater")
elif c>a and c >b and c>d:
    print("c is greater")
else:
    print("d is greater")
    