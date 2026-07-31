#Wap to find a product of n numbers
n=int(input("Number:"))
i=1
product=1
while i<=n:
    product*=i
    i+=1
print(product)