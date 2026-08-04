#WAP to print the prime number
n=int(input("n:"))
if n<=1:
    print("not prime")
else:
    i=2
    while i<n:
        if n%i==0:
            print("not prime")
            break
        i+=1
    else:
        print("prime")
        