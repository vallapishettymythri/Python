#find smallest and largest digit in the number using for loop
n=int(input("enter value:"))
temp=n
count=0
while temp>0:
    count+=1
    temp//=10
small=large=n%10
for i in range(count):
    digit=n%10
    if(digit>large):
        large=digit
    if digit < small:
        small=digit
    n//=10
print(large,small)