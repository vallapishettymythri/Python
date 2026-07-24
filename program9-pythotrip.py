#find pythogoras triplets
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if ((a**2)==(b**2)+(c**2)) or ((b**2)==(a**2)+(b**2)) or ((c**2)==(a**2)+(b**2)):
    print("a,b,c are pythogoras triplets")
else:
    print("a,b,c are not pythogoras triplets")

