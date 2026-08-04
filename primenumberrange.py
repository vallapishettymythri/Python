#Print a prime number between specific range
st=int(input("start:"))
end=int(input("end:"))
while st<=end:
    i=2
    while i<st:
        if st%i==0:
            break
        i+=1
    if i==st:
        print(st)
    st+=1
