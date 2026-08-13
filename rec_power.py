#WAP to find the power of a number using recursion- o(n)
def pow(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,(b-1))
a=int(input("a:"))
b=int(input("b:"))
pow(a,b)
