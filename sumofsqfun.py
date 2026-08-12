#WAP to perform a sum of square of n no using function
def square(n):
    sum=0
    for i in range(1,n+1):
        sum+=i**2
    return sum