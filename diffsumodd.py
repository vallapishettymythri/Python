#WAP to find the difference in the sum of even and odd of the n numbers
n=int(input("Number:"))
i=1
evensum=0
oddsum=0
while i<=n:
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i
    i+=1
difference=evensum-oddsum
print(difference)