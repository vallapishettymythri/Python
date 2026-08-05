#rotate k value of number using while loop
n=int(input("enter values:"))
k=int(input("k:"))
temp=n
count=0
while temp>0:
    count+=1
    temp//=10
last=n%(10**k)
first=n//(10**k)
shift=10**(count-k)
answer=last*shift+first
print(answer)
    