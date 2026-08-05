#wap to find the product of digit using for loop
#method 3- using math to import log10
from math import log10
n=int(input("enter values:"))
product=1
count=int(log10(n))+1
for i in range(count):
    digit=n%10
    product*=digit
    n//=10
print(product)