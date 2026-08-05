#wap to find the product of digit using while loop
n=int(input("enter values:"))
product=1
while n>0:
    digit=n%10
    product*=digit
    n//=10
print(product)