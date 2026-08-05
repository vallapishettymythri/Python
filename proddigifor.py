#wap to find the product of digit using for loop
#method 2- using while to count + for loop
n=int(input("enter values:"))
temp=n
product=1
count=0
while temp>0:
    count+=1
    temp//=10
for i in range(count):
    digit=n%10
    product*=digit
    n//=10
print(product)
