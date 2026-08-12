#WAP to find the sum of digits using recurssion
def sum_digi(n):
    if n==0:
        return 0
    else:
        return n%10+sum_digi(n//10)
n=int(input("n:"))
sum_digi(n)
