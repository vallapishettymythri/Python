#WAP to print a product of n numbers using recursion.(factorial)
def prod(n):
    if n==1:
        return 1
    else:
        return n*prod(n-1)
n=int(input("n:"))
prod(n)