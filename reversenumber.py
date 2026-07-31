#WAP to reverse a number
n=int(input("n:"))
rev=0
while n>0:
    digit=n%10
    rev=digit+rev*10
    n//=10
print(rev)