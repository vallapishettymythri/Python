#WAP to solve ncr using recursion
def prod(n):
    if n==1:
        return 1
    else:
        return n*prod(n-1)
def ncr(n,r):
    return prod(n)/(prod(r)*prod(n-r))
n=int(input("n:"))
r=int(input("r:"))
ncr(n,r)   