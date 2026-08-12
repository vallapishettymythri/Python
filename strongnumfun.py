#wap to check whether a number is a strong number or not.
def factorial(n):
    i=1
    fact=1
    while i<=n:
        fact*=i
        i+=1
    return fact
def check_strong_number(number):
    sum=0
    temp=number
    while temp>0:
        digit=temp%10
        sum+=factorial(digit)
        temp//=10
    if number==sum:
        return True
    else:
        return False
        

number=int(input("number:"))
check_strong_number(number)