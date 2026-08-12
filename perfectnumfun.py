#wap to check whether a number is a perfect number or not
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if i%2==0:
            sum+=i
    if n==sum:
        return True
    else:
        return False
        
        
n=int(input("n:"))
perfect_number(n)