#WAP to find the ncr
n=int(input("n value:"))
r=int(input("r value:"))
i=1
j=1
k=1
nfact=1
rfact=1
nminusr=n-r
nminusrfact=1
while i<=n:
    nfact*=i
    i+=1
while j<=r:
    rfact*=j
    j+=1
while k<=nminusr:
    nminusrfact*=k
    k+=1
ncr=nfact/(rfact*nminusrfact)
print(ncr)