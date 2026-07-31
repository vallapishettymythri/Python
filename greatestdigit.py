#WAP to find the greates digit in the number
n=int(input("n:"))
greatest=0
while n>0:
    digit=n%10
    if greatest<digit:
        greatest=digit
    n//=10
print(greatest)