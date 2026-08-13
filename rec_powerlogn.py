#o(logn)
def recursive_dnc(a,n):
    if n==0:
        return 1
    elif n%2==0:
        res= recursive_dnc(a,n//2)
        return res*res
    else:
        res= recursive_dnc(a,n//2)
        return a*res*res
a=int(input("a:"))
n=int(input("n:"))
recursive_dnc(a,n)