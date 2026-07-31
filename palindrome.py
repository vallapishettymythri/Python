#WAP to checke whether a number is palindrome or not
n=int(input("n:"))
rev=0
temp=n
while temp>0:
    digit=temp%10
    rev=digit+rev*10
    temp//=10
if n==rev:
    print("palindrome")
else:
    print("not palindrome")