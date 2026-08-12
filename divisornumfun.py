#WAP to print all the divisor of a number
def divisor(n):
    for i in range(1,n):
        if n%i==0:
            print(i)
divisor(6)