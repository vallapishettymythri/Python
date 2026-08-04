#Print all the armstrong numbers in specific range
st=int(input("st:"))
end=int(input("end:"))
while st<=end:
    temp=st
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if sum==st:
        print(st)
    st+=1