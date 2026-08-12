#wap to find the mean and standard deviation
def find_mean_sd(n):
    i=1
    sum=0
    variance=0
    while i<=n:
        sum+=i
        i+=1
    mean=sum/n
    for i in range(1,n+1):
        variance+=(i-mean)**2
    variance/=n
    sd=(variance)**0.5
    return mean,sd