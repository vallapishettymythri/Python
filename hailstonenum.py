#WAP to print hailstone number
n=int(input("n:"))
while n!=1:
    if n%2==0:
        n//=2
        print(n)
    else:
        n=3*n+1
        print(n)