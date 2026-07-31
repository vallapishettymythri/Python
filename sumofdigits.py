#WAP to find the sum of the digits of a number
n=int(input("n:"))
sum=0
i=1
while i <=n:
    digit=n%10
    n//=10
    sum+=digit
print(sum)
    